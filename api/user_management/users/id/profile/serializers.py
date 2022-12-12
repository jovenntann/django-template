from rest_framework import serializers

# Models
from domain.users.models import User, Profile


class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "UserManagementUsersIdProfile_ReadUserSerializer"
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
            'password': {'write_only': True}
        }


class ReadProfileSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "UserManagementUsersIdProfile_ReadProfileSerializer"
        model = Profile
        fields = [
            'id',
            'user',
            'bio',
            'location',
            'birth_date'
        ]


class ReadUserProfileSerializer(serializers.ModelSerializer):

    profile = ReadProfileSerializer(read_only=True)

    class Meta:
        ref_name = "UserManagementUsersIdProfile_ReadUserProfileSerializer"
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'profile'
        ]
