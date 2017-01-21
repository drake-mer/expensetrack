from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from django.views.decorators.csrf import csrf_exempt

from pprint import pformat

from ..models import BookUser

@csrf_exempt
def get_session( request ):
    """
    Send a login request
    """
    user = BookUser.objects.get_by_natural_key(request.POST['login'])

    login( request.POST['login'], request.POST['password'] )

    return HttpResponse(f"""
    GET_LOGIN_FOR_ID {user.id}
    """)