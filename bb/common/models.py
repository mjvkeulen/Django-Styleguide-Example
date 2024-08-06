from django.db import models
from django.db.models import F, Q
from django.utils import timezone


class BaseModel(models.Model):
    """
    We want to have the following behavior:

    1. created_at is set by default, but can be overridden.
    2. updated_at is not set on initial creation (stays None).
    3. The service layer (check `model_update`) takes care of providing value to `updated_at`,
        if there's no value provided by the caller.
    """
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SimpleModel(models.Model):
    """
    This is a basic model used to illustrate a many-to-many relationship
    with RandomModel.
    """

    name = models.CharField(max_length=255, blank=True, null=True)


class RandomModel(BaseModel):
    """
    This is an example model, to be used as reference in the Styleguide,
    when discussing model validation via constraints.
    """

    start_date = models.DateField()
    end_date = models.DateField()

    simple_objects = models.ManyToManyField(
        SimpleModel, blank=True, related_name="random_objects"
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="start_date_before_end_date", check=Q(start_date__lt=F("end_date"))
            )
        ]
