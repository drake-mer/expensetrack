from django.shortcuts import render
import django.http as dj
from django.views.decorators.csrf import csrf_exempt
import rest_framework.response as rest
from rest_framework import status
from django.views.decorators.http import require_POST
from django.forms.models import model_to_dict

from pprint import pformat

from ..models import BookUser

# Create your views here.

@csrf_exempt
def get_users(request):
    """
    Get the list of all users.
    You must be authenticated as an admin to perform this operation.
    """
    list_id = {str(user.id): user.username for user in BookUser.objects.all()}
    return dj.JsonResponse(list_id)


@csrf_exempt
def create_user(request):
    """
    Create an user with info provided within the HTTP request.

    Authentication is not needed to use this method
    """
    username = request.POST['username']
    user_info = {
        key: request.POST.get(key, None)
        for key in ['first_name', 'last_name', 'password', 'email']
    }

    my_user = BookUser.objects.create_user( username, **user_info )
    return dj.HttpResponse(f"""CREATE USER REQUEST OK: ID={my_user.id}""")


@csrf_exempt
def update_user(request, user_id):
    """
    Update an user with the given information
    :param request: HttpRequest
    :param user_id: Primary Key of the user being modified
    :return:
    """
    return dj.HttpResponse(f"""UPDATE_USER_REQUEST OK ID={user_id}""")


@csrf_exempt
def get_user_from_id(request, user_id: int):
    """
    Retrieve the user info from the user_id given as argument.
    You must be an admin to access this data or the corresponding user
    """
    try:
        u = BookUser.objects.get(pk=user_id)
    except BookUser.DoesNotExist:
        raise dj.Http404("Unable to find this user")
    else:
        # return the user fields as a dictionary
        return dj.JsonResponse(u.to_dict())


@csrf_exempt
def delete_user_from_id(request, user_id: int):
    """
    Delete the specified user from the user_id given as an argument.
    You must be authenticated as an admin to be able to perform this operation
    """
    try:
        u = BookUser.objects.get( pk=user_id )
        u.delete()
    except BookUser.DoesNotExist:
        return dj.HttpResponseNotFound()
    else:
        return dj.HttpResponse( status=status.HTTP_204_NO_CONTENT )
