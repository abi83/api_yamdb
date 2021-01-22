from rest_framework import permissions


class AuthorPermissions(permissions.BasePermission):
    """Редактирование объекта возможно только для Автора."""
    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user == obj.author)
