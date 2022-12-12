# Tests
from django.test import TestCase
from rest_framework.test import APIClient

from .test_utils import generate_token, create_user_object, create_admin_user_object

import json
import logging

logger = logging.getLogger(__name__)


class UsersAPIViewCreateTestCase(TestCase):

    def test_normal_user_should_not_be_able_to_create_a_user(self):
        """As a Normal User, I Should not be able to create a user"""
        create_user_object()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = '/user-management/users'
        data = {
            'username': 'juan',
            'password': 'Pass@12345',
            'first_name': 'Juan',
            'last_name': 'Dela Cruz',
            'email': 'juan@old.st'
        }
        response = client.post(path, data)
        content = json.loads(response.content)

        self.assertEqual({
            'detail': 'You do not have permission to perform this action.'
        }, content)
        self.assertEqual(403, response.status_code)

    def test_admin_should_be_able_to_create_a_user(self):
        """As admin, I Should be able to create a user"""
        create_admin_user_object()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = '/user-management/users'
        data = {
            'username': 'juan',
            'password': 'Pass@12345',
            'first_name': 'Juan',
            'last_name': 'Dela Cruz',
            'email': 'juan@old.st'
        }
        response = client.post(path, data)
        content = json.loads(response.content)

        self.assertEqual({
            'id': content['id'],
            'username': 'juan',
            'first_name': 'Juan',
            'last_name': 'Dela Cruz',
            'email': 'juan@old.st'
        }, content)


class UsersAPIViewGetTestCase(TestCase):

    def test_normal_user_should_not_be_able_to_get_all_users(self):
        """As a Normal User, I Should not be able to get all users"""
        create_user_object()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = '/user-management/users'
        response = client.get(path)
        content = json.loads(response.content)

        self.assertEqual({
            'detail': 'You do not have permission to perform this action.'
        }, content)
        self.assertEqual(403, response.status_code)

    def test_admin_should_get_all_users(self):
        """As admin, I Should be able to get all users"""
        user_object = create_admin_user_object()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = '/user-management/users'
        response = client.get(path)
        content = json.loads(response.content)

        self.assertIn({
            'id': user_object.pk,
            'username': 'root',
            'first_name': 'Super',
            'last_name': 'Admin',
            'email': 'root@old.st',
        }, content['results'])
