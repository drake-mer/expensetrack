from django.http.response import DjangoJSONEncoder
from django.http.response import HttpResponse, HttpResponseNotFound, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from ..models import BookUser
from ..serializers import MetaBookUserSerializer, BookUserSerializer

# Create your views here.

class BookUserViewAsList(APIView):

    def get(self, request):
        users = BookUser.objects.all()
        serializer = MetaBookUserSerializer(users, many=True)
        return JS


        """
        Retrieve the user info from the user_id given as argument.
        You must be an admin to access this data or the corresponding user
        """
        try:
            u = BookUser.objects.get(pk=user_id)
        except BookUser.DoesNotExist:
            raise Http404("Unable to find this user")
        else:
            # return the user fields as a dictionary
            return JsonResponse(u.to_dict())

    @csrf_exempt
    def delete(self, request, user_id: int):
        """
        Delete the specified user from the user_id given as an argument.
        You must be authenticated as an admin to be able to perform this operation
        """
        try:
            u = BookUser.objects.get(pk=user_id)
            u.delete()
        except BookUser.DoesNotExist:
            return HttpResponseNotFound()
        else:
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET'])
def get_users(request):
    """
    Get the list of all users.
    You must be authenticated as an admin to perform this operation.
    """
    users = BookUser.objects.all()
    serializer = BookUserSerializer(users)
    return JSONResponse(serializer.data)


@csrf_exempt
@api_view(['POST'])
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
    return HttpResponse(f"""CREATE USER REQUEST OK: ID={my_user.id}""")


@csrf_exempt
@api_view(['PUT'])
def update_user(request, user_id):
    """
    Update an user with the given information
    :param request: HttpRequest
    :param user_id: Primary Key of the user being modified
    :return:
    """
    return HttpResponse(f"""UPDATE_USER_REQUEST OK ID={user_id}""")


@csrf_exempt
@api_view(['GET'])
def get_user_from_id(request, user_id: int):
    """
    Retrieve the user info from the user_id given as argument.
    You must be an admin to access this data or the corresponding user
    """
    try:
        u = BookUser.objects.get(pk=user_id)
    except BookUser.DoesNotExist:
        raise Http404("Unable to find this user")
    else:
        serializer=MetaBookUserSerializer(u)
        return JsonResponse(serializer.data)


@csrf_exempt
@api_view(['DELETE'])
def delete_user_from_id(request, user_id: int):
    """
    Delete the specified user from the user_id given as an argument.
    You must be authenticated as an admin to be able to perform this operation
    """
    try:
        u = BookUser.objects.get( pk=user_id )
        u.delete()
    except BookUser.DoesNotExist:
        return HttpResponseNotFound()
    else:
        return HttpResponse( status=status.HTTP_204_NO_CONTENT )
