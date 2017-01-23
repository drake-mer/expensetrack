from django.contrib.auth.models import User

from rest_framework import serializers

from restbook.models import Record

class UserSerializer(serializers.ModelSerializer):
    records = serializers.PrimaryKeyRelatedField(many=True, queryset=Record.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'records')

class RecordSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Record
        fields = ('id',
                  'owner'
                  'record_date',
                  'user_date',
                  'user_time',
                  'value',
                  'description',
                  'comment')