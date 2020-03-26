import random
import string

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from users.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('username'), unique=True, max_length=255)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email

    def save(self, **kwargs):
        # if User is being created, generate new username
        if not self.id:
            highest_id_user = CustomUser.objects.order_by('id').last()
            next_id = highest_id_user.id if highest_id_user else 1
            random_string = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=6))
            self.username = '{}{}'.format(random_string, next_id)
        super().save(**kwargs)
