from rest_framework import serializers

# Models
from domain.products.models import Product, Category

import logging
logger = logging.getLogger(__name__)


class ReadCategorySerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "ProductManagementProducts_ReadCategorySerializer"
        model = Category
        fields = [
            'id',
            'name',
            'description',
            'created_at',
            'updated_at'
        ]


class ReadProductSerializer(serializers.ModelSerializer):

    categories = ReadCategorySerializer(many=True)

    class Meta:
        ref_name = "ProductManagementProducts_ReadProductSerializer"
        model = Product
        fields = [
            'id',
            'store',
            'categories',
            'title',
            'description',
            'created_at',
            'updated_at'
        ]


class CreateProductSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "ProductManagementProducts_CreateProductSerializer"
        model = Product
        fields = [
            'store',
            'categories',
            'title',
            'description'
        ]


class PaginateReadProductSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "ProductManagementProducts_PaginateReadProductSerializer"

    count = serializers.IntegerField()
    next = serializers.URLField()
    previous = serializers.URLField()
    results = ReadProductSerializer(many=True)


class PaginateQueryReadProductSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "ProductManagementProducts_PaginateQueryReadProductSerializer"

    page = serializers.IntegerField(required=False, help_text="A page number within the paginated result set.")
