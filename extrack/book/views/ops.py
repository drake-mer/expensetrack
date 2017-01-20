from django.shortcuts import render
from django.http import HttpResponse
from ..models import User, Record


def get_all_record_of_user(request):
    return HttpResponse("OK")

# Create your views here.
def get_all_record_of_user_between(request):
    return HttpResponse("OK")

# Create your views here.
def append_new_record_to_user(request):
    return HttpResponse("OK")


def delete_last_record_of_user(request):
    return HttpResponse("OK")

