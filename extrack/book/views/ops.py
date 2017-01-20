from django.shortcuts import render
from django.http import HttpResponse
from ..models import User, Record


def get_records(request, user_id: int):
    """
    Get all the records of a given User_Id.
    You must have logged in successfully as that user or to be an admin
    """
    return HttpResponse(f"""
    GET_ALL_RECORDS_FROM_USER ID {user_id}
    """)


def get_record_from_id(request, record_id: int):
    """
    Get the record details from the record ID
    """
    return HttpResponse(f"REQUEST_SINGLE_RECORD ID {record_id}")


def update_record_from_id( request, record_id: int):
    """
    :param request: incoming HttpRequest
    :param request_id:
    :return:
    """
    return HttpResponse(f"REQUEST_UPDATE_SINGLE_RECORD ID {record_id}")


def get_records_by_user_by_week(request, user_id: int, week: int, year: int):
    """
    Get all the record made by a particular user for a given week.
    You must be authenticated as that user or be an admin to access
    this view.
    """
    return HttpResponse("REQUEST_RECORDS_BY_USER_BY_WEEK "
                        "USER {user_id} YEAR {year} WEEK {week}")


def delete_record(request, record_id: int):
    """
    Delete this record based on the record_id. The authenticated
    client must own this record or be an admin to execute this action.
    """
    return HttpResponse(f"DELETE_RECORD_REQUEST ID {record_id}")


# Create your views here.
def add_record(request, user_id: int):
    """
    Add a record as an user.
    You must be an authenticated user to execute this action or an admin.
    """
    return HttpResponse(f"ADD_RECORD_REQUEST USER_ID {user_id}")


