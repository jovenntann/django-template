from rest_framework import serializers

# Models
from django.contrib.auth.models import User


class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "UserManagementUsersId_ReadUserSerializer"
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email'
        ]


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "UserManagementUsersId_UpdateUserSerializer"
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        ]


class DeleteUserSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "UserManagementUsersId_DeleteUserSerializer"

    operation = serializers.CharField(max_length=100)
    domain = serializers.CharField(max_length=200)
    model = serializers.CharField(max_length=100)
    data = ReadUserSerializer()
