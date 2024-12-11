from rest_framework import permissions


class IsActiveEmployees(permissions.BasePermission):
    """Проверяет, является ли пользователь активным сотрудником."""

    def has_permission(self, request, view):
        return request.user.groups.filter(name='active employees').exists()
