from django.shortcuts import render
from django.http import HttpResponse

from ..models import User

# Create your views here.
def get_all_users(request):
    return HttpResponse("OK")

# Create your views here.
def get_last_registered_user(request):
    return HttpResponse("OK")

# Create your views here.
def delete_last_registered_user(request):
    return HttpResponse("OK")

def delete_all_users(request):
    return HttpResponse("OK")
