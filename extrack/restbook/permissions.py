from rest_framework import permissions


class UserManagementListLevel(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):

        # anything is allowed for an admin
        if request.user and request.user.is_staff:
            return True
        else:
            return False



class UserManagementDetailLevel(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):

        # anything is allowed for an admin
        if request.user and request.user.is_staff:
            return True

        # only allow to access data if it is the user account
        elif obj.id == request.user.id:
            return True

        else:
            return False


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admin to create an user but
    to be read only on the list of users if one is only a logged in user
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return False
        else:
            return False
