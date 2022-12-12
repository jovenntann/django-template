from typing import List

# Models
from django.contrib.auth.models import User

# Django
from django.contrib.auth.hashers import make_password

import logging
logger = logging.getLogger(__name__)


def get_users() -> List[User]:
    user_objects = User.objects.all().order_by('id')
    logger.info(f"{user_objects} fetched")
    return user_objects


def get_user_by_id(user_id: int) -> User:
    user_object = User.objects.filter(id=user_id).first()
    logger.info(f"{user_object} fetched")
    return user_object


def delete_user_by_object(user_object: User) -> User:
    user_object.delete()
    logger.info(f"{user_object} has been deleted.")
    return user_object


def create_user(
    username: str,
    first_name: str,
    last_name: str,
    email: str,
    password: str
) -> User:
    # validated_data['password'] = make_password(validated_data['password'])
    # return User.objects.create(**validated_data)
    user_object = User.objects.create(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=make_password(password)
    )
    logger.info(f"\"{user_object}\" has been created.")
    return user_object


def update_user_by_object(
        user_object: User,
        username: str,
        first_name: str,
        last_name: str,
        email: str,
        password: str
) -> User:
    user_object.username = username
    user_object.first_name = first_name
    user_object.last_name = last_name
    user_object.email = email
    user_object.password = make_password(password)
    user_object.save()

    logger.info(f"\"{user_object}\" has been updated.")
    return user_object

