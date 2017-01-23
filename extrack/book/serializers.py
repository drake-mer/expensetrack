from django.http import HttpResponse

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import BookUser, Record


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)



class MetaBookUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookUser
        fields = ('user_id', 'username', 'first_name', 'last_name', 'password')

class MetaRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ('user_id', 'record_date', 'user_date', 'user_time',
                  'value', 'description', 'comment')



class BookUserSerializer( serializers.Serializer ):
    user_id = serializers.IntegerField(read_only=True)
    record_date = serializers.DateTimeField(read_only=True)
    user_date = serializers.DateField(required=False)
    user_time = serializers.TimeField(required=False)
    value = serializers.DecimalField( required=False,
                                      decimal_places=2, max_digits=50 )
    description = serializers.CharField( required=False, allow_blank=False, max_length=50 )
    comment = serializers.CharField( required=False, allow_blank=True, max_length=200 )

    def create(self, validated_data):
        return BookUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user_date = validated_data.get('user_date', instance.user_date)
        instance.user_time = validated_data.get('user_time', instance.user_time)
        instance.value = validated_data.get('value', instance.value)
        instance.description = validated_data.get('description', instance.description)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.save()
        return instance

