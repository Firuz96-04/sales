from rest_framework.permissions import BasePermission


class CategoryOnlyAdmin(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff and request.user.role_id == 1)
