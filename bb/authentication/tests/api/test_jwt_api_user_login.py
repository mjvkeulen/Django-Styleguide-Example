from http import HTTPStatus

from django.conf import settings
from django.test import Client, TestCase
from django.urls import reverse

from bb.users.models import User
from bb.users.services import user_create


# TODO STACK: Convert to using Ninja JWT
class UserJwtLoginTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()

        # TODO STACK: These are derived from the package Ninja JWT, what is the reverse url lookup?
        cls.jwt_login_url = "/api/token/pair"
        cls.jwt_refresh_token_url = "/api/token/refresh"
        cls.jwt_verify_token = "/api/token/verify"
        cls.me_url = reverse("api-1.0.0:authentication_me")
        cls.user_credentials = {
            "username": "test@app.brainbooster.nl",
            "password": "brainbooster",
        }

    def test_non_existing_user_cannot_obtain_jwt_token_pair(self):
        assert User.objects.count() == 0

        response = self.client.post(self.jwt_login_url, self.user_credentials, content_type="application/json")

        assert response.status_code == HTTPStatus.UNAUTHORIZED

    def test_existing_user_can_login_and_access_apis(self):
        """
        1. Create user
        2. Assert login is OK
        3. Call /api/users/me
        4. Assert valid response
        """
        user_create(**{"email": "test@app.brainbooster.nl", **self.user_credentials})

        response = self.client.post(self.jwt_login_url, self.user_credentials, content_type="application/json")
        assert response.status_code == HTTPStatus.OK
        data = response.json()
        assert data.get("access")
        assert data.get("refresh")

        response = self.client.get(self.me_url)
        assert response.status_code, HTTPStatus.UNAUTHORIZED

        auth_headers = {"HTTP_AUTHORIZATION": f"Bearer {data.get("access")}"}
        response = self.client.get(self.me_url, **auth_headers)
        assert response.status_code, HTTPStatus.OK
