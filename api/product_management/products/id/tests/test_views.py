# Tests
from django.test import TestCase
from rest_framework.test import APIClient

from .test_utils import generate_token, create_user_object, \
    create_store_object, create_category_object, create_product_object

import json
import logging

logger = logging.getLogger(__name__)


class ProductsIdAPIViewGetTestCase(TestCase):

    def test_should_return_404_for_getting_not_existing_product(self):
        """Should return 404 for getting not existing product"""
        create_user_object()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        not_existing_product_id = 10
        path = f"/product-management/products/{not_existing_product_id}"
        response = client.get(path)

        self.assertEqual(404, response.status_code)

    def test_should_be_able_get_a_product(self):
        """Should be able to get a product"""
        user_object = create_user_object()
        store_object = create_store_object(user_object)
        category_object = create_category_object()
        product_object = create_product_object(store_object, category_object)

        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = f"/product-management/products/{product_object.id}"
        response = client.get(path)
        content = json.loads(response.content)

        self.assertEqual({
            'id': product_object.id,
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
            'created_at': str(product_object.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
            'updated_at': str(product_object.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
        }, content)


class ProductsIdAPIViewDeleteTestCase(TestCase):

    def test_should_return_404_for_deleting_not_existing_product(self):
        """Should return 404 for deleting not existing product"""
        create_user_object()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        not_existing_product_id = 10
        path = f"/product-management/products/{not_existing_product_id}"
        response = client.delete(path)

        self.assertEqual(404, response.status_code)

    def test_should_be_able_delete_a_product(self):
        """Should be able to delete a product"""
        user_object = create_user_object()
        store_object = create_store_object(user_object)
        category_object = create_category_object()
        product_object = create_product_object(store_object, category_object)

        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = f"/product-management/products/{product_object.id}"
        response = client.delete(path)
        content = json.loads(response.content)
        logger.info(content)
        self.assertEqual({
            'operation': 'delete',
            'domain': 'products',
            'model': 'Product',
            'data': {
                'id': product_object.id,
                'store': store_object.id,
                'categories': [{
                    "id": category_object.id,
                    "name": category_object.name,
                    "description": category_object.description,
                    'created_at': str(category_object.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
                    'updated_at': str(category_object.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
                }],
                'title': 'iPhone',
                'description': 'Best Phone',
                'created_at': str(product_object.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
                'updated_at': str(product_object.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
            }
        }, content)


class ProductsIdAPIViewUpdateTestCase(TestCase):

    def test_should_return_404_for_updating_not_existing_product(self):
        """Should return 404 for updating not existing product"""
        create_user_object()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        not_existing_product_id = 10
        path = f"/product-management/products/{not_existing_product_id}"
        data = {
            'store': 1,
            'categories': 1,
            'title': 'Android',
            'description': 'Best Android',
        }
        response = client.put(path, data)

        self.assertEqual(404, response.status_code)

    def test_should_be_able_update_a_product(self):
        """Should be able to update a product"""
        user_object = create_user_object()
        store_object = create_store_object(user_object)
        category_object = create_category_object()
        product_object = create_product_object(store_object, category_object)

        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = f"/product-management/products/{product_object.id}"
        data = {
            'store': store_object.id,
            'categories': [category_object.id],
            'title': 'Android',
            'description': 'Best Android',
        }
        response = client.put(path, data)
        content = json.loads(response.content)
        self.assertEqual({
            'id': product_object.id,
            'store': store_object.id,
            'categories': [{
                "id": category_object.id,
                "name": category_object.name,
                "description": category_object.description,
                'created_at': str(category_object.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
                'updated_at': str(category_object.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
            }],
            'title': 'Android',
            'description': 'Best Android',
            'created_at': str(product_object.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
            'updated_at': content['updated_at']
        }, content)


class ProductsIdAPIViewPatchTestCase(TestCase):

    def test_should_return_404_for_patching_not_existing_product(self):
        """Should return 404 for patching not existing product"""
        create_user_object()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        not_existing_product_id = 10
        path = f"/product-management/products/{not_existing_product_id}"
        data = {
            'store': 1,
            'categories': 1,
            'title': 'Android',
            'description': 'Best Android',
        }
        response = client.patch(path, data)

        self.assertEqual(404, response.status_code)

    def test_should_be_able_patch_a_product(self):
        """Should be able to patch a product"""
        user_object = create_user_object()
        store_object = create_store_object(user_object)
        category_object = create_category_object()
        product_object = create_product_object(store_object, category_object)

        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = f"/product-management/products/{product_object.id}"
        data = {
            'title': 'iPhone',
            'description': 'Best iPhone',
        }
        response = client.patch(path, data)
        content = json.loads(response.content)
        self.assertEqual({
            'id': product_object.id,
            'store': store_object.id,
            'categories': [{
                "id": category_object.id,
                "name": category_object.name,
                "description": category_object.description,
                'created_at': str(category_object.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
                'updated_at': str(category_object.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
            }],
            'title': 'iPhone',
            'description': 'Best iPhone',
            'created_at': str(product_object.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
            'updated_at': content['updated_at']
        }, content)
