# Tests
from django.test import TestCase
from rest_framework.test import APIClient

from .test_utils import generate_token, create_user_object

import json
import logging

logger = logging.getLogger(__name__)


class UsersIdAPIViewGetTestCase(TestCase):

    def test_should_return_404_for_getting_not_existing_user(self):
        """Should return 404 for getting not existing user"""
        create_user_object()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        not_existing_user_id = 999
        path = f"/user-management/users/{not_existing_user_id}"
        response = client.get(path)

        self.assertEqual(404, response.status_code)

    def test_should_be_able_get_a_user(self):
        """Should be able to get a user"""
        user_object = create_user_object()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = f"/user-management/users/{user_object.pk}"
        response = client.get(path)
        content = json.loads(response.content)
        self.assertEqual({
            'id': content['id'],
            'username': 'root',
            'first_name': 'Super',
            'last_name': 'Admin',
            'email': 'root@old.st'
        }, content)


class UsersIdAPIViewDeleteTestCase(TestCase):

    def test_should_return_404_for_deleting_not_existing_user(self):
        """Should return 404 for deleting not existing user"""
        create_user_object()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        not_existing_user_id = 999
        path = f"/user-management/users/{not_existing_user_id}"
        response = client.delete(path)

        self.assertEqual(404, response.status_code)

    def test_should_be_able_delete_a_user(self):
        """Should be able to delete a user"""
        user_object = create_user_object()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = f"/user-management/users/{user_object.pk}"
        response = client.delete(path)
        content = json.loads(response.content)
        self.assertEqual({
            'operation': 'delete',
            'domain': 'users',
            'model': 'User',
            'data': {
                'id': user_object.pk,
                'username': 'root',
                'first_name': 'Super',
                'last_name': 'Admin',
                'email': 'root@old.st'
            }
        }, content)


class UsersIdAPIViewUpdateTestCase(TestCase):

    def test_should_return_404_for_updating_not_existing_user(self):
        """Should return 404 for updating not existing user"""
        create_user_object()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        not_existing_user_id = 999
        path = f"/user-management/users/{not_existing_user_id}"
        data = {
            "username": "root2",
            "password": "09106850350",
            'first_name': 'Super2',
            'last_name': 'Admin2',
            'email': 'root2@old.st'
        }
        response = client.put(path, data)

        self.assertEqual(404, response.status_code)

    def test_should_be_able_update_a_user(self):
        """Should be able to update a user"""
        user_object = create_user_object()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = f"/user-management/users/{user_object.pk}"
        data = {
            "username": "root2",
            "password": "09106850350",
            'first_name': 'Super2',
            'last_name': 'Admin2',
            'email': 'root2@old.st'
        }
        response = client.put(path, data)
        content = json.loads(response.content)
        self.assertEqual({
            'id': user_object.pk,
            'username': 'root2',
            'first_name': 'Super2',
            'last_name': 'Admin2',
            'email': 'root2@old.st'
        }, content)


class UsersIdAPIViewPatchTestCase(TestCase):

    def test_should_return_404_for_patching_not_existing_user(self):
        """Should return 404 for patching not existing user"""
        create_user_object()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        not_existing_user_id = 999
        path = f"/user-management/users/{not_existing_user_id}"
        data = {
            'first_name': 'Super2',
            'last_name': 'Admin2'
        }
        response = client.patch(path, data)

        self.assertEqual(404, response.status_code)

    def test_should_be_able_patch_a_user(self):
        """Should be able to patch a user"""
        user_object = create_user_object()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = f"/user-management/users/{user_object.pk}"
        data = {
            'first_name': 'Super2',
            'last_name': 'Admin2',
        }
        response = client.patch(path, data)
        content = json.loads(response.content)
        self.assertEqual({
            'id': user_object.pk,
            'username': 'root',
            'first_name': 'Super2',
            'last_name': 'Admin2',
            'email': 'root@old.st'
        }, content)
