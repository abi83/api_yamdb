from rest_framework import permissions
from users_api.models import YamdbUser


class AuthorPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method not in permissions.SAFE_METHODS:
            return request.user.role == YamdbUser.Role.MODERATOR or request.user == obj.author
        return True


# class IsAdminPermissions(permissions.BasePermission):
#
#     def has_object_permission(self, request, view, obj):
#         if request.method not in permissions.SAFE_METHODS:
#             return request.user.role == YamdbUser.Role.ADMIN or YamdbUser.Role.MODERATOR
#         return True
#
#     def has_permission(self, request, view):
#         if request.user.role == YamdbUser.Role.ADMIN or YamdbUser.Role.MODERATOR:
#             return True
