from django.test import TestCase

from domain.users.tests.utils.utils import create_user_object

from domain.stores.models import Store

from ...models import Category
from ...models import Product

from ...services.service_Product import get_products, get_product_by_id, delete_product_by_object, \
    create_product, update_product_by_object


# Create your tests here.
class ServiceProductGetProductsTestCase(TestCase):

    def test_should_be_able_to_get_all_products(self):
        """Should return all products"""
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

        product_objects = get_products()
        self.assertEqual({
            'id': product_object.id,
            'store': store_object.id,
            'categories': product_object.categories,
            'title': 'iPhone',
            'description': 'Best Phone',
            'created_at': product_object.created_at,
            'updated_at': product_object.updated_at
        }, {
            'id': product_objects[0].id,
            'store': product_objects[0].store.id,
            'categories': product_objects[0].categories,
            'title': product_objects[0].title,
            'description': product_objects[0].description,
            'created_at': product_objects[0].created_at,
            'updated_at': product_objects[0].updated_at
        })


class ServiceProductGetProductByIdTestCase(TestCase):

    def test_should_return_none_if_product_id_do_not_exist(self):
        """Should return None if category id do not exist"""
        not_existing_product_id = 999
        product_object = get_product_by_id(not_existing_product_id)
        self.assertIsNone(product_object)

    def test_should_be_able_to_get_product_by_id(self):
        """Should be able to get product object by id"""
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

        product_object_by_id = get_product_by_id(product_object.id)
        self.assertEqual({
            'id': product_object.id,
            'store': store_object.id,
            'categories': product_object.categories,
            'title': 'iPhone',
            'description': 'Best Phone',
            'created_at': product_object.created_at,
            'updated_at': product_object.updated_at
        }, {
            'id': product_object_by_id.id,
            'store': product_object_by_id.store.id,
            'categories': product_object_by_id.categories,
            'title': product_object_by_id.title,
            'description': product_object_by_id.description,
            'created_at': product_object_by_id.created_at,
            'updated_at': product_object_by_id.updated_at
        })


class ServiceProductDeleteProductByObjectTestCase(TestCase):

    def test_should_be_able_to_delete_product_by_object(self):
        """Should be able to delete product by object"""
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

        deleted_product_object = delete_product_by_object(product_object)
        self.assertEqual(product_object, deleted_product_object)


class ServiceProductCreateProductTestCase(TestCase):

    def test_should_be_able_create_product(self):
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
        product_object = create_product(
            store_object,
            [category_object.id],
            'iPhone',
            'Best Phone'
        )

        self.assertEqual({
            'id': product_object.id,
            'store': store_object.id,
            'categories': product_object.categories,
            'title': 'iPhone',
            'description': 'Best Phone',
            'created_at': product_object.created_at,
            'updated_at': product_object.updated_at
        }, {
            'id': product_object.id,
            'store': product_object.store.id,
            'categories': product_object.categories,
            'title': product_object.title,
            'description': product_object.description,
            'created_at': product_object.created_at,
            'updated_at': product_object.updated_at
        })


class ServiceProductUpdateProductByObjectTestCase(TestCase):

    def test_should_be_able_update_product(self):
        """Should be able to update a product"""
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

        update_product_object = update_product_by_object(
            product_object,
            store_object,
            [category_object.id],
            'iPhone',
            'Best Phone'
        )

        self.assertEqual({
            'id': product_object.id,
            'store': store_object.id,
            'categories': product_object.categories,
            'title': 'iPhone',
            'description': 'Best Phone',
            'created_at': product_object.created_at,
            'updated_at': product_object.updated_at
        }, {
            'id': update_product_object.id,
            'store': update_product_object.store.id,
            'categories': update_product_object.categories,
            'title': update_product_object.title,
            'description': update_product_object.description,
            'created_at': update_product_object.created_at,
            'updated_at': update_product_object.updated_at
        })
