from http import HTTPStatus

from django.test import Client, TestCase
from django.urls import reverse

from bb.users.models import User
from bb.users.services import user_create


class UserSessionLoginTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()

        cls.session_login_url = reverse("api-1.0.0:authentication_session_login")
        cls.session_logout_url = reverse("api-1.0.0:authentication_session_logout")
        cls.me_url = reverse("api-1.0.0:authentication_me")
        cls.user_credentials = {
            "username": "test@app.brainbooster.nl",
            "password": "brainbooster",
        }

    def test_non_existing_user_cannot_login(self):
        assert User.objects.count() == 0

        response = self.client.post(self.session_login_url, data=self.user_credentials, content_type="application/json")

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert "No active account found matching these credentials." in response.json()["message"]

    def test_existing_user_can_login_and_access_apis(self):
        """
        1. Create user
        2. Assert login is OK
        3. Call /api/auth/me
        4. Assert valid response
        """
        user_create(**{"email": "test@app.brainbooster.nl", **self.user_credentials})

        response = self.client.post(self.session_login_url, data=self.user_credentials, content_type="application/json")

        assert response.status_code == HTTPStatus.OK
        data = response.json()
        session = data["session"]
        assert session is not None

        response = self.client.get(self.me_url)
        assert response.status_code == HTTPStatus.OK

        # Now, try without session attached to the client
        client = Client()
        response = client.get(self.me_url)
        # TODO STACK: Discuss with team if this should (across auth flows) be 401 or 403
        assert response.status_code == HTTPStatus.UNAUTHORIZED

        response = client.get(self.me_url, headers={"Authorization": f"Session {session}"})
        assert response.status_code == HTTPStatus.OK

    def test_existing_user_can_logout(self):
        """
        1. Create user
        2. Login, can access APIs
        3. Logout, cannot access APIs
        """
        user_create(**{"email": "test@app.brainbooster.nl", **self.user_credentials})

        response = self.client.post(self.session_login_url, data=self.user_credentials, content_type="application/json")
        assert response.status_code == HTTPStatus.OK

        response = self.client.get(self.me_url)
        assert response.status_code == HTTPStatus.OK

        self.client.post(self.session_logout_url)

        response = self.client.get(self.me_url)
        assert response.status_code == HTTPStatus.UNAUTHORIZED
