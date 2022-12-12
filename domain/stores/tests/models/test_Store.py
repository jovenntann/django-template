from django.test import TestCase
from ...models import Store
from django.contrib.auth.models import User

import logging
logger = logging.getLogger(__name__)


# Create your tests here.
class ModelStoreTestCase(TestCase):
    def setUp(self):
        self.user_object = User.objects.create(username="root")
        self.store_object = Store.objects.create(
            user=self.user_object,
            name="Apple",
            contact_number="+1023456789",
            address="California"
        )

    # def tearDown(self):
    #     self.user_object.delete()
    #     self.store_object.delete()

    def test_get_excerpt(self):
        """Should return first few characters of the address"""
        result = self.store_object.get_excerpt(5)
        self.assertEqual('Calif', result)

    def test_store_str(self):
        self.assertEqual('Apple', str(self.store_object))

    def test_should_be_able_to_create_store(self):
        """Should be able to create a store"""
        store_object = Store.objects.create(
            user=self.user_object,
            name="Apple",
            contact_number="+1023456789",
            address="California"
        )
        self.assertEqual({
            'user': self.user_object.pk,
            'name': 'Apple',
            'contact_number': '+1023456789',
            'address': 'California'
        }, {
            'user': self.user_object.pk,
            'name': store_object.name,
            'contact_number': store_object.contact_number,
            'address': store_object.address
        })
