"""
NB : this code won't probably be published in the final app
It's just an additional step in the creation process
"""

from django.contrib.auth.models import User
from django.http import HttpResponse, Http404

from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions

from restbook.models import Record
from restbook.serializers import RecordSerializer, UserSerializer

class RecordList(APIView):
    """
    List all the records
    """
    def get(self, request, format=None):
        records = Record.objects.all()
        serializer = RecordSerializer( records, many=True )
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RecordSerializer( data=request.data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RecordDetail(APIView):
    """
    Retrieve, update or delete a record instance
    """
    def get_object(self, pk):
        try:
            return Record.objects.get(pk=pk)
        except Record.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        record = self.get_object(pk)
        serializer = RecordSerializer(record)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        record = self.get_object(pk)
        serializer = RecordSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        record = self.get_object(pk)
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

