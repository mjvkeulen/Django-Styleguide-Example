from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from bb.common.models import BaseModel


# TODO STACK: Just work with User as table
class User(AbstractUser, BaseModel):
    """
    Default custom user model for BrainBooster.
    """

    # First and last name do not cover name patterns around the globe
    full_name = models.CharField(_("Full name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore[assignment]
    last_name = None  # type: ignore[assignment]
