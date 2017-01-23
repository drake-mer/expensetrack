

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..models import Record, BookUser
from ..serializers import JSONResponse
from ..serializers import MetaRecordSerializer

@csrf_exempt
def get_records(request, user_id: int):
    """
    Get all the records of a given User_Id.
    You must have logged in successfully as that user or to be an admin
    """

    all = Record.objects.filter( user_id=user_id )
    serializer = MetaRecordSerializer(all, many=True)
    return JSONResponse(serializer.data)

@csrf_exempt
def get_record_from_id(request, record_id):
    """
    Get the record details from the record ID
    """
    all = Record.objects.filter( pk=int(record_id) )
    serializer = MetaRecordSerializer(all)
    return JSONResponse(serializer.data)


@csrf_exempt
def update_record_from_id( request, record_id: int):
    """
    :param request: incoming HttpRequest containing JSON data
    :param record_id: the id of the record to be modified
    :return: None
    """
    keys_to_update = [ 'user_date', 'user_time', 'value', 'description', 'comment' ]
    record = {
        key: request.POST.get(key, None)
        for key in ['record_id', 'user_date', 'user_time', 'value', 'description', 'comment']
    }
    if record['record_id'] is None:
        record['record_id']=record_id


    new_rec = Record.objects.get( pk=int(record['record_id']) )
    for key in filter( lambda k: record[k], keys_to_update ):
        new_rec.__setattr__(key, record[key])

    new_rec.save()
    return HttpResponse(f"UPDATE_RECORD SUCCESS {new_rec.id}")


@csrf_exempt
def get_records_by_user_by_week(request, user_id: int, week: int, year: int):
    """
    Get all the record made by a particular user for a given week.
    You must be authenticated as that user or be an admin to access
    this view.
    """
    return HttpResponse("REQUEST_RECORDS_BY_USER_BY_WEEK "
                        "USER {user_id} YEAR {year} WEEK {week}")


@csrf_exempt
def delete_record(request, record_id: int):
    """
    Delete this record based on the record_id. The authenticated
    client must own this record or be an admin to execute this action.
    """
    return HttpResponse(f"DELETE_RECORD_REQUEST ID {record_id}")


# Create your views here.
@csrf_exempt
def add_record(request, user_id: int):
    """
    Add a record as an user.
    You must be an authenticated user to execute this action.
    """
    record = {
        key: request.POST.get(key, None)
        for key in ['user_id', 'user_date', 'user_time', 'value', 'description', 'comment']
    }
    record['user_id'] = BookUser.objects.get( pk=int(record['user_id']) )
    my_rec = Record(**record)

    my_rec.save()
    return HttpResponse(f"ADD_RECORD_REQUEST SUCCESS {my_rec.id}")



