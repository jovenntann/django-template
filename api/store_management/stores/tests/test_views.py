from django.test import TestCase
from rest_framework.test import APIClient

# Utils
from .test_utils import generate_token, create_user_object

# Models
from domain.stores.models import Store

import json
import logging

logger = logging.getLogger(__name__)


class StoresAPIViewCreateTestCase(TestCase):

    def test_should_be_able_to_create_a_store(self):
        """Should be able to create a store"""
        user_object = create_user_object()
        access_token = generate_token()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = '/store-management/stores'
        data = {
            'name': 'Apple Store',
            'contact_number': '09062131607',
            'address': 'California'
        }
        response = client.post(path, data)
        content = json.loads(response.content)
        logger.info(content)
        self.assertEqual({
            'id': content['id'],
            'user': user_object.pk,
            'name': 'Apple Store',
            'contact_number': '09062131607',
            'address': 'California',
            'created_at': content['created_at'],
            'updated_at': content['updated_at']
        }, content)
        
        
class StoresAPIViewGetTestCase(TestCase):

    def test_should_be_able_to_get_all_stores(self):
        """Should be able to get all the stores"""
        user_object = create_user_object()
        access_token = generate_token()

        store_object = Store.objects.create(
            user=user_object,
            name="Apple Store",
            contact_number="09062131607",
            address="California"
        )

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = '/store-management/stores'
        response = client.get(path)
        content = json.loads(response.content)

        self.assertIn({
            'id': store_object.id,
            'user': user_object.pk,
            'name': store_object.name,
            'contact_number': store_object.contact_number,
            'address': store_object.address,
            'created_at': str(store_object.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
            'updated_at': str(store_object.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")),
        }, content['results'])
