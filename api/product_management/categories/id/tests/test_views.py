# Tests
from django.test import TestCase
from rest_framework.test import APIClient

from .test_utils import generate_token, create_user_object, create_category_object

import json
import logging

logger = logging.getLogger(__name__)


class CategoriesIdAPIViewGetTestCase(TestCase):

    def test_should_return_404_for_not_existing_category(self):
        """Should return 404 for not existing product"""
        create_user_object()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        not_existing_category_id = 10
        path = f"/product-management/categories/{not_existing_category_id}"
        response = client.get(path)

        self.assertEqual(404, response.status_code)

    def test_should_be_able_to_get_a_category(self):
        """Should be able to get a category"""
        create_user_object()
        category_object = create_category_object()

        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = f"/product-management/categories/{category_object.id}"
        response = client.get(path)
        content = json.loads(response.content)

        self.assertEqual({
            'id': category_object.id,
            'name': 'Phones',
            'description': 'All kind of phones',
            'created_at': str(category_object.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
            'updated_at': str(category_object.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
        }, content)


class CategoriesIdAPIViewDeleteTestCase(TestCase):

    def test_should_return_404_for_deleting_not_existing_category(self):
        """Should return 404 for deleting not existing category"""
        create_user_object()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        not_existing_category_id = 10
        path = f"/product-management/categories/{not_existing_category_id}"
        response = client.delete(path)
        self.assertEqual(404, response.status_code)

    def test_should_be_able_to_delete_a_category(self):
        """Should be able to delete a category"""
        create_user_object()
        category_object = create_category_object()

        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = f"/product-management/categories/{category_object.id}"
        response = client.delete(path)
        content = json.loads(response.content)
        self.assertEqual({
            'operation': 'delete',
            'domain': 'products',
            'model': 'Category',
            'data': {
                'id': category_object.id,
                'name': 'Phones',
                'description': 'All kind of phones',
                'created_at': str(category_object.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
                'updated_at': str(category_object.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
            }
        }, content)


class CategoriesIdAPIViewUpdateTestCase(TestCase):

    def test_should_return_404_for_updating_not_existing_category(self):
        """Should return 404 for updating not existing category"""
        create_user_object()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        not_existing_category_id = 10
        path = f"/product-management/categories/{not_existing_category_id}"
        data = {
            'name': 'Laptop',
            'description': 'All kind of laptop',
        }
        response = client.put(path, data)
        self.assertEqual(404, response.status_code)

    def test_should_be_able_to_update_a_category(self):
        """Should be able to update a category"""
        create_user_object()
        category_object = create_category_object()

        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = f"/product-management/categories/{category_object.id}"
        data = {
            'name': 'Laptop',
            'description': 'All kind of laptop',
        }
        response = client.put(path, data)
        content = json.loads(response.content)
        self.assertEqual({
            'id': category_object.id,
            'name': 'Laptop',
            'description': 'All kind of laptop',
            'created_at': content['created_at'],
            'updated_at': content['updated_at']
        }, content)


class CategoriesIdAPIViewPatchTestCase(TestCase):

    def test_should_return_404_for_patching_not_existing_category(self):
        """Should return 404 for patching not existing category"""
        create_user_object()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        not_existing_category_id = 10
        path = f"/product-management/categories/{not_existing_category_id}"
        data = {
            'name': 'Laptop',
            'description': 'All kind of laptop',
        }
        response = client.patch(path, data)
        self.assertEqual(404, response.status_code)

    def test_should_be_able_to_patched_a_category(self):
        """Should be able to patched a category"""
        create_user_object()
        category_object = create_category_object()

        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = f"/product-management/categories/{category_object.id}"
        data = {
            'description': 'All kinds of iPhone',
        }
        response = client.patch(path, data)
        content = json.loads(response.content)
        self.assertEqual({
            'id': category_object.id,
            'name': 'Phones',
            'description': 'All kinds of iPhone',
            'created_at': content['created_at'],
            'updated_at': content['updated_at']
        }, content)
