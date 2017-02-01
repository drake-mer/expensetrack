from rest_framework import permissions
from django.contrib.auth.models import User as UserModel

class UserManagementListLevel(permissions.BasePermission):
    """
    This permission class only allows an admin user to access the list of users.
    Only an admin user can create users.
    """

    def has_permission(self, request, view):

        # anything is allowed for an admin
        if request.user and request.user.is_authenticated:
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



class RecordManagementDetailLevel(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):

        # anything is allowed for an admin
        if request.user and request.user.is_staff:
            return True

        # only allow to access data if it is the user's record
        elif obj.owner == request.user:
            return True

        else:
            return False


class RecordManagementListLevel(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_permission(self, request, view):

        # anything is allowed for an admin
        the_user = request.user # type: UserModel
        if the_user.is_authenticated:
            return True
        else:
            return False

