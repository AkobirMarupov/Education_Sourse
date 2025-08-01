from rest_framework.permissions import BasePermission

class IsCenterAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_center_admin
