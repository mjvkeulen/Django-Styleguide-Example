from django.db import models
from django.db.models import F, Q
from django.utils import timezone


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    # TODO STACK: Discuss and decide on its ideal handling (automatic vs manual)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
