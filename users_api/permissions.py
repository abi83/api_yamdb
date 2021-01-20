from rest_framework import permissions
from users_api.models import YamdbUser


class IsYamdbAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.is_superuser or request.user.role == YamdbUser.Role.ADMIN

        return False


class IsYamdbModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        # breakpoint()
        if request.user.is_authenticated:
            return request.user.is_superuser or request.user.role == YamdbUser.Role.MODERATOR

        return False


class IsYamdbCategoryAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated:
            return request.user.is_superuser or request.user.role == YamdbUser.Role.ADMIN

        return False
