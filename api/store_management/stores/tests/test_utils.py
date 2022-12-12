import json

from rest_framework.test import APIClient

# Models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


def create_user_object() -> User:
    user_object = User.objects.create(
        username="root",
        password=make_password('09106850351'),
        first_name="Super",
        last_name="Admin",
        email="root@old.st"
    )
    return user_object


def generate_token():
    client = APIClient()
    path = '/authentication/token/'
    data = {
        "username": "root",
        "password": "09106850351"
    }
    response = client.post(path, data)
    content = json.loads(response.content)
    access_token = content['access']
    return access_token
