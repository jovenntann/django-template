from rest_framework import serializers
from domain.users.models import Profile


class ReadProfileSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "AuthenticatedProfile_ReadProfileSerializer"
        model = Profile
        fields = [
            'id',
            'user',
            'bio',
            'location',
            'birth_date'
        ]
