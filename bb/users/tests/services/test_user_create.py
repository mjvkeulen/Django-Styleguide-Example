from django.test import TestCase

from bb.users.services import user_create


class UserCreateTests(TestCase):
    def test_user_without_password_is_created_with_unusable_one(self):
        user = user_create(username="random_user@app.brainboost.nl", email="random_user@app.brainboost.nl")

        self.assertFalse(user.has_usable_password())
