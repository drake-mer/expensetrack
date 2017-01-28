from collections import OrderedDict

from django.contrib.auth.models import User

from rest_framework import serializers

from restbook.models import Record



class UserSerializer(serializers.ModelSerializer):
    records = serializers.PrimaryKeyRelatedField(many=True, queryset=Record.objects.all())
    records_to_skip = ('password')

    class Meta:
        model = User
        fields = ('id', 'username', 'records', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def update(self, instance, validated_data):
        """Must override update method for password specific stuff"""
        new_instance = super().update(instance=instance, validated_data=validated_data)
        password = validated_data.get('password', None)
        if password:
            new_instance.set_password(password)
            new_instance.save()

        return new_instance

class RecordSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField( source='owner.username' )

    class Meta:
        model = Record
        fields = ('id',
                  'owner',
                  'record_date',
                  'user_date',
                  'user_time',
                  'value',
                  'description',
                  'comment')