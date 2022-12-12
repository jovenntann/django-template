from rest_framework import serializers

# Models
from django.contrib.auth.models import User


class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "UserManagementUsers_ReadUserSerializer"
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email'
        ]


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "UserManagementUsers_CreateUserSerializer"
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        ]

        extra_kwargs = {
            'email': {'required': True},
            'password': {'write_only': True}
        }


class PaginateUserSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "UserManagementUsers_PaginateUserSerializer"

    count = serializers.IntegerField()
    next = serializers.URLField()
    previous = serializers.URLField()
    results = ReadUserSerializer(many=True)


class PaginateQueryUserSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "UserManagementUsers_PaginateQueryUserSerializer"

    page = serializers.IntegerField(required=False, help_text="A page number within the paginated result set.")
