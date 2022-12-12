from django.test import TestCase

from domain.stores.models import Store

from ...models import Category
from ...models import Product

from domain.users.tests.utils.utils import create_user_object

import logging
logger = logging.getLogger(__name__)


# Create your tests here.
class ModelProductTestCase(TestCase):
    def test_should_be_able_to_create_product(self):
        """Should be able to create a product"""
        user_object = create_user_object()
        store_object = Store.objects.create(
            user=user_object,
            name="Apple",
            contact_number="+1023456789",
            address="California"
        )
        category_object = Category.objects.create(
            name="Phones",
            description="All kind of phones"
        )
        product_object = Product.objects.create(
            store=store_object,
            title="iPhone",
            description="Best Phone"
        )
        product_object.categories.set([category_object])
        product_object.save()

        self.assertEqual({
            'user': user_object.pk,
            'store': store_object.id,
            'categories': product_object.categories,
            'title': 'iPhone',
            'description': 'Best Phone',
            'created_at': product_object.created_at,
            'updated_at': product_object.updated_at
        }, {
            'user': user_object.pk,
            'store': store_object.id,
            'categories': product_object.categories,
            'title': product_object.title,
            'description': product_object.description,
            'created_at': product_object.created_at,
            'updated_at': product_object.updated_at
        })
