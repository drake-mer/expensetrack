from rest_framework import serializers
from ..models import BookUser, Record

class BookUserSerializer( serializers.Serializer ):
    user_id = serializers.IntegerField(read_only=True)
    record_date = serializers.DateTimeField(read_only=True)
    user_date = serializers.DateField(required=False, allow_blank=False)
    user_time = serializers.TimeField(required=False, allow_blank=False)
    value = serializers.DecimalField(required=False, allow_blank=False)
    description = serializers.CharField( required=False, allow_blank=False, max_length=50 )
    comment = models.CharField( required=False, allow_blank=True, max_length=200 )

    def create(self, validated_date):
        return BookUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user_date = validated_data.get('user_date', instance.user_date)
        instance.user_time = validated_data.get('user_time', instance.user_time)
        instance.value = validated_data.get('value', instance.value)
        instance.description = validated_data.get('description', instance.description)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.save()
        return instance