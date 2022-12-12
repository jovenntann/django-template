from django.test import TestCase

from ...models import Store

# Utils
from domain.users.tests.utils.utils import create_user_object

# Services
from ...services.service_Store import get_stores, get_store_by_id, create_store, delete_store_by_object, update_store_by_object

import logging
logger = logging.getLogger(__name__)


# Create your tests here.
class ServiceStoreGetStoresTestCase(TestCase):

    def test_should_be_able_to_get_all_stores(self):
        """Should return all Stores"""
        user_object = create_user_object()
        store_object = Store.objects.create(
            user=user_object,
            name="Apple Store",
            contact_number="09062131607",
            address="California"
        )

        store_objects = get_stores()

        self.assertEqual({
            'id': store_object.id,
            'name': store_object.name,
            'contact_number': store_object.contact_number,
            'address': store_object.address,
            'created_at': store_object.created_at,
            'updated_at': store_object.updated_at
        }, {
            'id': store_objects[0].id,
            'name': store_objects[0].name,
            'contact_number': store_objects[0].contact_number,
            'address': store_objects[0].address,
            'created_at': store_objects[0].created_at,
            'updated_at': store_objects[0].updated_at
        })


class ServiceStoreCreateStoreTestCase(TestCase):

    def test_should_be_able_create_store(self):
        """Should be able to create a store"""
        user_object = create_user_object()
        store_object = create_store(
            user_object,
            'Apple Store',
            '09062131607',
            'California'
        )

        self.assertEqual({
            'id': store_object.id,
            'name': 'Apple Store',
            'contact_number': '09062131607',
            'address': 'California',
            'created_at': store_object.created_at,
            'updated_at': store_object.updated_at
        }, {
            'id': store_object.id,
            'name': store_object.name,
            'contact_number': store_object.contact_number,
            'address': store_object.address,
            'created_at': store_object.created_at,
            'updated_at': store_object.updated_at
        })


class ServiceStoreGetStoreByIdTestCase(TestCase):

    def test_should_return_none_if_category_id_do_not_exist(self):
        """Should return None if category id do not exist"""
        user_object = create_user_object()
        Store.objects.create(
            user=user_object,
            name="Apple Store",
            contact_number="09062131607",
            address="California"
        )
        not_existing_store_id = 99
        store_object = get_store_by_id(not_existing_store_id)
        self.assertIsNone(store_object)

    def test_should_be_able_to_get_store_by_id(self):
        """Should be able to get store object by id"""
        user_object = create_user_object()
        store_object = Store.objects.create(
            user=user_object,
            name="Apple Store",
            contact_number="09062131607",
            address="California"
        )
        store_object_by_id = get_store_by_id(store_object.id)
        self.assertEqual({
            'id': store_object.id,
            'name': 'Apple Store',
            'contact_number': '09062131607',
            'address': 'California',
            'created_at': store_object.created_at,
            'updated_at': store_object.updated_at
        }, {
            'id': store_object_by_id.id,
            'name': store_object_by_id.name,
            'contact_number': store_object_by_id.contact_number,
            'address': store_object_by_id.address,
            'created_at': store_object_by_id.created_at,
            'updated_at': store_object_by_id.updated_at
        })


class ServiceStoreDeleteStoreByObjectTestCase(TestCase):

    def test_should_be_able_to_delete_category_by_object(self):
        """Should be able to delete store by object"""
        user_object = create_user_object()
        store_object = Store.objects.create(
            user=user_object,
            name="Apple Store",
            contact_number="09062131607",
            address="California"
        )
        delete_store_object = delete_store_by_object(store_object)
        self.assertEqual(store_object, delete_store_object)


class ServiceProductUpdateProductByObjectTestCase(TestCase):

    def test_should_be_able_update_product(self):
        """Should be able to update a product"""
        user_object = create_user_object()
        store_object = Store.objects.create(
            user=user_object,
            name="Apple",
            contact_number="09106850351",
            address="California"
        )

        update_store_object = update_store_by_object(
            store_object,
            user_object,
            'Samsung Store',
            '09239108311',
            'Los Angeles'
        )

        self.assertEqual({
            'id': store_object.id,
            'user': user_object.pk,
            'name': 'Samsung Store',
            'contact_number': '09239108311',
            'address': 'Los Angeles',
            'created_at': store_object.created_at,
            'updated_at': store_object.updated_at
        }, {
            'id': update_store_object.id,
            'user': update_store_object.user.pk,
            'name': update_store_object.name,
            'contact_number': update_store_object.contact_number,
            'address': update_store_object.address,
            'created_at': update_store_object.created_at,
            'updated_at': update_store_object.updated_at
        })
