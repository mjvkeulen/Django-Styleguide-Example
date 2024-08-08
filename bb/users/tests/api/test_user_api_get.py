from django.conf import settings
from django.test import Client, TestCase
from django.urls import reverse

from bb.users.models import User
from bb.users.services import user_create


class UserApiGetTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()

        cls.user_get_url = reverse("api-1.0.0:user_get", args=[1])

    def test_user_get(self):
        # TODO STACK
        pass
        # How to handle AUTH
