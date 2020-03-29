import os

from django.conf import settings
from django.db import models
from django.dispatch import receiver


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


class ExampleThree(models.Model):
    """
    Example for media and image field with upload_to.
    Example for new lines in description field (use TextField).
    Example for deletion of a file from filesystem when corresponding model instance is deleted or updated with a new file.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon = models.ImageField(blank=True, null=True, upload_to='icons')


@receiver(models.signals.post_delete, sender=ExampleThree)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `ExampleThree` object is deleted.
    """
    if instance.icon:
        if os.path.isfile(instance.icon.path):
            os.remove(instance.icon.path)


@receiver(models.signals.pre_save, sender=ExampleThree)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `ExampleThree` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).icon
    except sender.DoesNotExist:
        return False

    if not old_file:
        return False

    new_file = instance.icon
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
