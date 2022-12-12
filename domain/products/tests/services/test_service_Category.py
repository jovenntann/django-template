from django.test import TestCase

from ...models import Category

from ...services.service_Category import get_categories, get_category_by_id, \
    delete_category_by_object, create_category, update_category_by_object


# Create your tests here.
class ServiceCategoryGetCategoriesTestCase(TestCase):

    def test_should_be_able_to_get_all_categories(self):
        """Should return all categories"""
        category_object = Category.objects.create(
            name='Shoes',
            description='All kind of shoes'
        )
        category_objects = get_categories()
        self.assertEqual({
            'id': category_object.id,
            'name': 'Shoes',
            'description': 'All kind of shoes',
            'created_at': category_object.created_at,
            'updated_at': category_object.updated_at
        }, {
            'id': category_objects[0].id,
            'name': category_objects[0].name,
            'description': category_objects[0].description,
            'created_at': category_objects[0].created_at,
            'updated_at': category_objects[0].updated_at
        })


class ServiceCategoryGetCategoryByIdTestCase(TestCase):

    def test_should_return_none_if_category_id_do_not_exist(self):
        """Should return None if category id do not exist"""
        Category.objects.create(
            name='Shoes',
            description='All kind of shoes'
        )
        not_existing_category_id = 99
        category_object = get_category_by_id(not_existing_category_id)
        self.assertIsNone(category_object)

    def test_should_be_able_to_get_category_by_id(self):
        """Should be able to get category object by id"""
        category_object = Category.objects.create(
            name='Shoes',
            description='All kind of shoes'
        )
        category_object_by_id = get_category_by_id(category_object.id)
        self.assertEqual({
            'id': category_object.id,
            'name': 'Shoes',
            'description': 'All kind of shoes',
            'created_at': category_object.created_at,
            'updated_at': category_object.updated_at
        }, {
            'id': category_object_by_id.id,
            'name': category_object_by_id.name,
            'description': category_object_by_id.description,
            'created_at': category_object_by_id.created_at,
            'updated_at': category_object_by_id.updated_at
        })


class ServiceCategoryDeleteCategoryByObjectTestCase(TestCase):

    def test_should_be_able_to_delete_category_by_object(self):
        """Should be able to delete user by object"""
        category_object = Category.objects.create(
            name='Shoes',
            description='All kind of shoes'
        )
        deleted_category_object = delete_category_by_object(category_object)
        self.assertEqual(category_object, deleted_category_object)


class ServiceCategoryCreateCategoryTestCase(TestCase):

    def test_should_be_able_create_category(self):
        """Should be able to create a category"""
        category_object = create_category('Shoes', 'All kind of shoes')

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


class ServiceCategoryUpdateCategoryTestCase(TestCase):

    def test_should_be_able_to_update_category(self):
        """Should be able to update a category"""
        category_object = Category.objects.create(
            name='Shoes',
            description='All kind of shoes'
        )
        update_category_object = update_category_by_object(
            category_object,
            name='Shirts',
            description='All kind of shirts'
        )
        self.assertEqual({
            'id': category_object.id,
            'name': 'Shirts',
            'description': 'All kind of shirts',
            'created_at': category_object.created_at,
            'updated_at': category_object.updated_at
        }, {
            'id': update_category_object.id,
            'name': update_category_object.name,
            'description': update_category_object.description,
            'created_at': update_category_object.created_at,
            'updated_at': update_category_object.updated_at
        })
