from django.conf import settings
from django.db import models


class ExampleOne(models.Model):
    """
    Example for viewsets and unique validation in serializer.
    """
    field_one = models.CharField(max_length=100)
    field_two = models.CharField(max_length=100)
    last_edit_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='edited_example_ones'
    )


class ExampleTwo(models.Model):
    """
    Example for disabling admin edit if instance not created today.
    """
    field_one = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
