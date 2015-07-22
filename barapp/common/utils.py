from django.contrib.auth.models import Permission


def add_permission(permission=None, user=None):
    if user and permission:
        permission = Permission.objects.get(name='Can {0}'.format(permission))
        user.user_permissions.add(permission)
