# DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Serializers
from .serializers import ReadUserSerializer, UpdateUserSerializer, DeleteUserSerializer

# Services
from domain.users.services.service_User import get_user_by_id, delete_user_by_object, update_user_by_object

# Django Shortcuts
from django.http import Http404

# Library: drf-yasg
from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


# TODO: User Permission (Cause this section might only useful for Administrator or Moderator)

class UsersIdAPIView(APIView):

    permission_classes = (IsAuthenticated,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: ReadUserSerializer()
        },
        operation_description="description",
        operation_id="users_read.",
        tags=["user-management"],
    )
    def get(request, user_id=None):
        logger.info(f"authenticated: {request.user}")
        user_object = get_user_by_id(user_id)
        if user_object is None:
            raise Http404
        user_serializer = ReadUserSerializer(user_object)
        return Response(user_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        operation_description="description",
        operation_id="users_delete",
        tags=["user-management"],
        responses={
            200: DeleteUserSerializer()
        }
    )
    def delete(request, user_id=None):
        logger.info(f"authenticated: {request.user}")
        user_object = get_user_by_id(user_id)
        if user_object is None:
            raise Http404
        # Copy user_object so that we can return this data from our delete response
        response = {
            'operation': 'delete',
            'domain': 'users',
            'model': 'User',
            'data': user_object
        }
        response_serializer = DeleteUserSerializer(response)
        response_serializer_data = response_serializer.data

        delete_user_by_object(user_object)

        return Response(response_serializer_data)

    @staticmethod
    @swagger_auto_schema(
        operation_description="description",
        operation_id="users_update",
        tags=["user-management"],
        request_body=UpdateUserSerializer,
        responses={
            200: ReadUserSerializer()
        }
    )
    def put(request, user_id=None):
        logger.info(f"authenticated: {request.user}")
        user_object = get_user_by_id(user_id)
        if user_object is None:
            raise Http404
        user_serializer = UpdateUserSerializer(
            data=request.data
        )
        if user_serializer.is_valid(raise_exception=True):
            user_object = update_user_by_object(
                user_object,
                user_serializer.validated_data.get('username', user_object.username),
                user_serializer.validated_data.get('first_name', user_object.first_name),
                user_serializer.validated_data.get('last_name', user_object.last_name),
                user_serializer.validated_data.get('email', user_object.email),
                user_serializer.validated_data.get('password', user_object.password)
            )
            # NOTE: Re-serialize to fetch more detailed data
            user_serializer = ReadUserSerializer(user_object)
            return Response(user_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        operation_description="description",
        operation_id="users_patch",
        tags=["user-management"],
        request_body=UpdateUserSerializer,
        responses={
            200: ReadUserSerializer()
        }
    )
    def patch(request, user_id=None):
        logger.info(f"authenticated: {request.user}")
        user_object = get_user_by_id(user_id)
        if user_object is None:
            raise Http404
        user_serializer = UpdateUserSerializer(
            data=request.data,
            partial=True
        )
        if user_serializer.is_valid(raise_exception=True):
            user_object = update_user_by_object(
                user_object,
                user_serializer.validated_data.get('username', user_object.username),
                user_serializer.validated_data.get('first_name', user_object.first_name),
                user_serializer.validated_data.get('last_name', user_object.last_name),
                user_serializer.validated_data.get('email', user_object.email),
                user_serializer.validated_data.get('password', user_object.password)
            )
            # NOTE: Re-serialize to fetch more detailed data
            user_serializer = ReadUserSerializer(user_object)
            return Response(user_serializer.data)

