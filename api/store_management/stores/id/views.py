# DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Serializers
from .serializers import ReadStoreSerializer, DeleteStoreSerializer, UpdateStoreSerializer

# Services
from domain.stores.services.service_Store import get_store_by_id, delete_store_by_object, update_store_by_object

# Django Shortcuts
from django.shortcuts import get_object_or_404
from django.http import Http404

# Library: drf-yasg
from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


# TODO: User Permission (Cause this section might only useful for Administrator or Moderator)

class StoresIdAPIView(APIView):

    permission_classes = (IsAuthenticated,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: ReadStoreSerializer()
        },
        operation_description="description",
        operation_id="stores_read",
        tags=["store-management"],
    )
    def get(request, store_id=None):
        logger.info(f"authenticated: {request.user}")
        store_object = get_store_by_id(store_id)
        if store_object is None:
            raise Http404
        store_serializer = ReadStoreSerializer(store_object)
        return Response(store_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        operation_description="description",
        operation_id="stores_delete",
        tags=["store-management"],
        responses={
            200: DeleteStoreSerializer()
        }
    )
    def delete(request, store_id=None):
        logger.info(f"authenticated: {request.user}")
        store_object = get_store_by_id(store_id)
        if store_object is None:
            raise Http404
        # Copy store_object so that we can return this data from our delete response
        response = {
            'operation': 'delete',
            'domain': 'stores',
            'model': 'Store',
            'data': store_object
        }
        response_serializer = DeleteStoreSerializer(response)
        response_serializer_data = response_serializer.data

        delete_store_by_object(store_object)

        return Response(response_serializer_data)

    @staticmethod
    @swagger_auto_schema(
        operation_description="description",
        operation_id="stores_update",
        tags=["store-management"],
        request_body=UpdateStoreSerializer,
        responses={
            200: ReadStoreSerializer()
        }
    )
    def put(request, store_id=None):
        logger.info(f"authenticated: {request.user}")

        store_object = get_store_by_id(store_id)
        if store_object is None:
            raise Http404

        store_serializer = UpdateStoreSerializer(
            data=request.data
        )
        if store_serializer.is_valid(raise_exception=True):
            update_store_by_object(
                store_object,
                request.user,
                store_serializer.validated_data.get('name', store_object.name),
                store_serializer.validated_data.get('contact_number', store_object.contact_number),
                store_serializer.validated_data.get('address', store_object.address)
            )
            # NOTE: Re-serialize to fetch more detailed data
            store_serializer = ReadStoreSerializer(
                store_object
            )
            return Response(store_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        operation_description="description",
        operation_id="stores_patch",
        tags=["store-management"],
        request_body=UpdateStoreSerializer,
        responses={
            200: ReadStoreSerializer()
        }
    )
    def patch(request, store_id=None):
        logger.info(f"authenticated: {request.user}")
        store_object = get_store_by_id(store_id)
        if store_object is None:
            raise Http404

        store_serializer = UpdateStoreSerializer(
            data=request.data,
            partial=True
        )
        if store_serializer.is_valid(raise_exception=True):
            update_store_by_object(
                store_object,
                request.user,
                store_serializer.validated_data.get('name', store_object.name),
                store_serializer.validated_data.get('contact_number', store_object.contact_number),
                store_serializer.validated_data.get('address', store_object.address),
            )
            store_serializer = ReadStoreSerializer(
                store_object
            )
            return Response(store_serializer.data)
