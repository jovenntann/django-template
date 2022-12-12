# Tests
from django.test import TestCase
from rest_framework.test import APIClient

from .test_utils import generate_token, create_user_object

# Models
from domain.stores.models import Store

import json
import logging

logger = logging.getLogger(__name__)


class StoresIdAPIViewGetTestCase(TestCase):

    def test_should_return_404_for_not_existing_store(self):
        """Should return 404 for not existing store"""
        create_user_object()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        not_existing_store_id = 999
        path = f"/store-management/stores/{not_existing_store_id}"
        response = client.get(path)

        self.assertEqual(404, response.status_code)

    def test_should_be_able_to_get_a_store(self):
        """Should be able to get a store"""
        user_object = create_user_object()
        store_object = Store.objects.create(
            user=user_object,
            name='Apple Store',
            contact_number='09106850351',
            address='California'
        )
        store_object.save()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = f"/store-management/stores/{store_object.id}"
        response = client.get(path)
        content = json.loads(response.content)

        self.assertEqual({
            'id': store_object.id,
            'user': user_object.pk,
            'name': 'Apple Store',
            'contact_number': '09106850351',
            'address': 'California',
            'created_at': str(store_object.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
            'updated_at': str(store_object.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
        }, content)


class StoresIdAPIViewDeleteTestCase(TestCase):

    def test_should_return_404_for_deleting_not_existing_store(self):
        """Should return 404 for deleting not existing store"""
        create_user_object()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        not_existing_store_id = 10
        path = f"/store-management/stores/{not_existing_store_id}"
        response = client.delete(path)
        self.assertEqual(404, response.status_code)

    def test_should_be_able_to_delete_a_store(self):
        """Should be able to delete a store"""
        user_object = create_user_object()
        store_object = Store.objects.create(
            user=user_object,
            name='Apple Store',
            contact_number='09106850351',
            address='California'
        )
        store_object.save()

        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = f"/store-management/stores/{store_object.id}"
        response = client.delete(path)
        content = json.loads(response.content)
        self.assertEqual({
            'operation': 'delete',
            'domain': 'stores',
            'model': 'Store',
            'data': {
                'id': store_object.id,
                'user': user_object.pk,
                'name': 'Apple Store',
                'contact_number': '09106850351',
                'address': 'California',
                'created_at': str(store_object.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
                'updated_at': str(store_object.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
            }
        }, content)


class StoresIdAPIViewUpdateTestCase(TestCase):

    def test_should_return_404_for_updating_not_existing_store(self):
        """Should return 404 for updating not existing store"""
        create_user_object()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        not_existing_store_id = 99
        path = f"/store-management/stores/{not_existing_store_id}"
        data = {
            'name': 'Samsung Store',
            'contact_number': '09239108311',
            'address': 'Los Angeles',
        }
        response = client.put(path, data)
        self.assertEqual(404, response.status_code)

    def test_should_be_able_to_update_a_store(self):
        """Should be able to update a store"""
        user_object = create_user_object()
        store_object = Store.objects.create(
            user=user_object,
            name='Apple Store',
            contact_number='09106850351',
            address='California'
        )

        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = f"/store-management/stores/{store_object.id}"
        data = {
            'name': 'Samsung Store',
            'contact_number': '09239108311',
            'address': 'Los Angeles',
        }
        response = client.put(path, data)
        content = json.loads(response.content)
        self.assertEqual({
            'id': store_object.id,
            'user': user_object.pk,
            'name': 'Samsung Store',
            'contact_number': '09239108311',
            'address': 'Los Angeles',
            'created_at': content['created_at'],
            'updated_at': content['updated_at']
        }, content)


class StoresIdAPIViewPatchTestCase(TestCase):

    def test_should_return_404_for_patching_not_existing_store(self):
        """Should return 404 for patching not existing store"""
        create_user_object()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        not_existing_store_id = 999
        path = f"/store-management/stores/{not_existing_store_id}"
        data = {
            'name': 'Samsung Store',
            'contact_number': '09239108311',
            'address': 'Los Angeles',
        }
        response = client.patch(path, data)
        self.assertEqual(404, response.status_code)

    def test_should_be_able_to_patch_a_store(self):
        """Should be able to patched a store"""
        user_object = create_user_object()
        store_object = Store.objects.create(
            user=user_object,
            name='Apple Store',
            contact_number='09106850351',
            address='California'
        )

        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = f"/store-management/stores/{store_object.id}"
        data = {
            'name': 'Samsung Store',
            'contact_number': '09239108311',
            'address': 'Los Angeles',
        }
        response = client.patch(path, data)
        content = json.loads(response.content)
        self.assertEqual({
            'id': store_object.id,
            'user': user_object.pk,
            'name': 'Samsung Store',
            'contact_number': '09239108311',
            'address': 'Los Angeles',
            'created_at': content['created_at'],
            'updated_at': content['updated_at']
        }, content)
