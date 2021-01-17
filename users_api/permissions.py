from rest_framework import permissions
# from users_api.models import YamdbUser


class IsYamdbAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.is_superuser or request.user.role in ['A', 'admin', "('A', 'admin')"]

        return False


class IsYamdbModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.is_superuser or request.user.role in ['M', 'moderator', "('M', 'moderator')"]

        return False
