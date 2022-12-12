# Tests
from django.test import TestCase
from rest_framework.test import APIClient

from .test_utils import generate_token, create_user_object, create_category_object

import json
import logging

logger = logging.getLogger(__name__)


class CategoriesAPIViewCreateTestCase(TestCase):

    def test_should_be_able_to_post_a_category(self):
        """Should be able to post a category"""
        create_user_object()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = '/product-management/categories'
        data = {
            'name': 'Phones',
            'description': 'All kind of phones'
        }
        response = client.post(path, data)
        content = json.loads(response.content)
        self.assertEqual({
            'id': content['id'],
            'name': 'Phones',
            'description': 'All kind of phones',
            'created_at': content['created_at'],
            'updated_at': content['updated_at']
        }, content)


class CategoriesAPIViewGetTestCase(TestCase):

    def test_should_be_able_to_get_all_categories(self):
        """Should be able to get all categories"""
        create_user_object()
        category_object = create_category_object()

        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = '/product-management/categories'
        response = client.get(path)
        content = json.loads(response.content)
        logger.info(content)

        self.assertIn({
            'id': category_object.id,
            'name': 'Phones',
            'description': 'All kind of phones',
            'created_at': str(category_object.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
            'updated_at': str(category_object.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
        }, content['results'])
