# Tests
from django.test import TestCase
from rest_framework.test import APIClient

from .test_utils import generate_token, create_user_object, \
    create_store_object, create_category_object, create_product_object

import json
import logging

logger = logging.getLogger(__name__)


class ProductsAPIViewCreateTestCase(TestCase):

    def test_should_be_able_to_post_a_product(self):
        """Should be able to post a product"""
        user_object = create_user_object()
        store_object = create_store_object(user_object)
        category_object = create_category_object()

        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = '/product-management/products'
        data = {
            'store': store_object.id,
            'categories': category_object.id,
            'title': 'iPhone',
            'description': 'Best Phone',
        }
        response = client.post(path, data)
        content = json.loads(response.content)
        self.assertEqual({
            'id': content['id'],
            'store': store_object.id,
            'categories': [{
                'id': category_object.id,
                'name': category_object.name,
                'description': category_object.description,
                'created_at': str(category_object.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
                'updated_at': str(category_object.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
            }],
            'title': 'iPhone',
            'description': 'Best Phone',
            'created_at': content['created_at'],
            'updated_at': content['updated_at']
        }, content)


class ProductsAPIViewGetTestCase(TestCase):

    def test_should_be_able_to_get_all_products(self):
        """Should be able to get all products"""
        user_object = create_user_object()
        store_object = create_store_object(user_object)
        category_object = create_category_object()
        product_object = create_product_object(store_object, category_object)

        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = '/product-management/products'
        response = client.get(path)
        content = json.loads(response.content)

        self.assertIn({
            'id': product_object.id,
            'store': store_object.id,
            'categories': [{
                "id": category_object.id,
                "name": category_object.name,
                "description": category_object.description,
                'created_at': str(category_object.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
                'updated_at': str(category_object.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
            }],
            'title': 'iPhone',
            'description': 'Best Phone',
            'created_at': str(product_object.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
            'updated_at': str(product_object.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
        }, content['results'])
