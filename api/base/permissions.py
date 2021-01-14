
from rest_framework import permissions


class CurrentUserOrAdminUser(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        user = request.user
        return obj == user or user.is_staff
