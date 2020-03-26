from django.conf import settings
from django.db import models

# Create your models here.


class ExampleOne(models.Model):
    field_one = models.CharField(max_length=100)
    field_two = models.CharField(max_length=100)
    last_edit_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='edited_example_ones'
    )
