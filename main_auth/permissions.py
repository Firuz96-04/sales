from rest_framework.permissions import BasePermission


class MyAdminUser(BasePermission):

    def has_permission(self, request, view):
        print(dir(request.user))
        return bool(request.user and request.user.is_staff and request.user.is_superuser)


class BuilderManagerPermission(BasePermission):

    def has_permission(self, request, view):
        # print(request.user.status == 'active')
        # print(request.user.id)
        # print(request.user.first_name,' 444')
        return bool(request.user and request.user.is_authenticated
                    and request.user.role.name == 'builder'
                    and request.user.status_id == 1)