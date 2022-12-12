from django.test import TestCase

from ...models import Category


import logging
logger = logging.getLogger(__name__)


# Create your tests here.
class ModelCategoryTestCase(TestCase):
    def test_should_be_able_to_create_category(self):
        """Should be able to create a category"""
        category_object = Category.objects.create(
            name='Shoes',
            description='All kind of shoes'
        )
        self.assertEqual({
            'id': category_object.id,
            'name': 'Shoes',
            'description': 'All kind of shoes',
            'created_at': category_object.created_at,
            'updated_at': category_object.updated_at
        }, {
            'id': category_object.id,
            'name': category_object.name,
            'description': category_object.description,
            'created_at': category_object.created_at,
            'updated_at': category_object.updated_at
        })
