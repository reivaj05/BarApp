from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


def validate_username_does_not_exists(username):
    try:
        if User.objects.get(username=username):
            raise ValidationError(
                'The username "%(username)s" already exists',
                code='user_already_exists',
                params={
                    'username': username
                }
                )
    except User.DoesNotExist:
        pass  # Username available


def validate_user_already_exists(username):
    try:
        User.objects.get(username=username)
    except User.DoesNotExist:
        raise ValidationError(
            'The "%(username)s" account does not exists',
            code='user_not_found',
            params={
                'username': username
            }
            )


def validate_user_is_active(username):
    try:
        user = User.objects.get(username=username)
        if user.is_active is False:
            raise ValidationError(
                'The account with username "%(username)s" is inactive',
                code='user_not_active',
                params={
                    'username': username
                }
                )
    except User.DoesNotExist:
        pass  # Already validated in validate_user_exists(username)