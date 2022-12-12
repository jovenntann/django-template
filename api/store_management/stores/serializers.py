from rest_framework import serializers

# Models
from domain.stores.models import Store

import logging
logger = logging.getLogger(__name__)


class ReadStoreSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "StoreManagementStores_ReadStoreSerializer"
        model = Store
        fields = [
            'id',
            'user',
            'name',
            'contact_number',
            'address',
            'created_at',
            'updated_at'
        ]


class CreateStoreSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "StoreManagementStores_CreateStoreSerializer"
        model = Store
        fields = [
            'name',
            'contact_number',
            'address'
        ]


class PaginateReadStoreSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "StoreManagementStores_PaginateReadStoreSerializer"

    count = serializers.IntegerField()
    next = serializers.URLField()
    previous = serializers.URLField()
    results = ReadStoreSerializer(many=True)

class PaginateQueryReadStoreSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "StoreManagementStores_PaginateQueryReadStoreSerializer"

    page = serializers.IntegerField(required=False, help_text="A page number within the paginated result set.")
