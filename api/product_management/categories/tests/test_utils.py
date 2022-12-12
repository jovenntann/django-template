import json

from rest_framework.test import APIClient

# Models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from domain.stores.models import Store
from domain.products.models import Product, Category


def create_user_object():
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


def generate_refresh_token():
    client = APIClient()
    path = '/authentication/token/'
    data = {
        "username": "root",
        "password": "09106850351"
    }
    response = client.post(path, data)
    content = json.loads(response.content)
    refresh_token = content['refresh']
    return refresh_token


def create_store_object(user_object):
    store_object = Store.objects.create(
        user=user_object,
        name="Apple",
        contact_number="+1023456789",
        address="California"
    )
    return store_object


def create_category_object():
    category_object = Category.objects.create(
        name="Phones",
        description="All kind of phones"
    )
    return category_object


def create_product_object(store_object, category_object):
    product_object = Product.objects.create(
        store=store_object,
        title='iPhone',
        description="Best Phone"
    )
    product_object.categories.set([category_object])
    product_object.save()
    return product_object
