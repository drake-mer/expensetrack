from django.shortcuts import render
from django.http import HttpResponse
from pprint import pformat

from ..models import BookUser

# Create your views here.

def get_users(request):
    """
    Get the list of all users.
    You must be authenticated as an admin to perform this operation.
    """
    return HttpResponse("""
    GET_ALL_USERS_REQUEST
    """)

def create_user(request):
    """
    Create an user with info provided within the HTTP request.

    Authentication is not needed to use this method
    """

    BookUser.objects.create_user( username='FAKE_LOGIN',
                                  first_name='FAKE_NAME',
                                  last_name='FAKE_LAST_NAME',
                                  password='*****')
    return HttpResponse("""
    CREATE USER REQUEST
    """)


def update_user(request, user_id):
    """
    Update an user with the given information
    :param request: HttpRequest
    :param user_id: Primary Key of the user being modified
    :return:
    """
    return HttpResponse(f"""
    UPDATE_USER_REQUEST ID {user_id}
    """)

def get_user_from_id(request, user_id: int):
    """
    Retrieve the user info from the user_id given as argument.
    You must be an admin to access this data or the corresponding user
    """
    return HttpResponse(f"""
    REQUEST_USER_FROM_ID, ID={user_id}
    """)


def delete_user_from_id(request, user_id: int):
    """
    Delete the specified user from the user_id given as an argument.
    You must be authenticated as an admin to be able to perform this operation
    """
    return HttpResponse(f"""
    DELETE_USER_WITH_ID, ID={user_id}
    """)
