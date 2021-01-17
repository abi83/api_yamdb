from rest_framework import permissions
from users_api.models import YamdbUser


class IsYamdbAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # breakpoint()
        if request.user.is_authenticated:
            return request.user.is_superuser or request.user.role == str(YamdbUser.ADMIN)

        return False


class IsYamdbModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.is_superuser or request.user.role == str(YamdbUser.MODERATOR)

        return False
