from rest_framework import permissions


class AuthorPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method not in permissions.SAFE_METHODS:
            return request.user.is_moderator or request.user == obj.author
        return True
