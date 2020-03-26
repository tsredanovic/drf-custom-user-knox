from datetime import timedelta

from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token


def token_expires_in(token):
    time_elapsed = timezone.now() - token.created
    left_time = timedelta(seconds=settings.TOKEN_LIFETIME_SECONDS) - time_elapsed
    return left_time


def token_is_expired(token):
    if not settings.TOKEN_LIFETIME_SECONDS:
        return False
    return token_expires_in(token) < timedelta(seconds=0)


def custom_create_token(token_model, user, serializer):
    token, _ = token_model.objects.get_or_create(user=user)
    is_expired = token_is_expired(token)
    if is_expired:
        token.delete()
        token = Token.objects.create(user=token.user)
    return token


class ExpiringTokenAuthentication(TokenAuthentication):
    """
    Adds expiration functionality to existing tokens.
    Controlled by TOKEN_LIFETIME_SECONDS setting.
    """

    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))

        # Check for token expiration
        is_expired = token_is_expired(token)
        if is_expired:
            raise exceptions.AuthenticationFailed(_('Expired token.'))

        return (token.user, token)
