from django.test import TestCase

from ..utils.utils import create_user_object

from ...services.service_User import get_users, get_user_by_id, \
    delete_user_by_object, create_user, update_user_by_object


# Create your tests here.
class ServiceUserGetUsersTestCase(TestCase):

    def test_should_be_able_to_get_all_users(self):
        """Should return all users"""
        user_object = create_user_object()
        user_objects = get_users()
        self.assertIn(user_object, user_objects)


class ServiceUserGetUserByIdTestCase(TestCase):

    def test_should_be_able_to_get_user_by_id(self):
        """Should be able to get user object by id"""
        user_object = create_user_object()
        user_object = get_user_by_id(user_object.pk)
        self.assertTrue(user_object)

    def test_should_return_none_if_user_id_do_not_exist(self):
        """Should return None if user id do not exist"""
        create_user_object()
        not_existing_user_id = 999
        user_object = get_user_by_id(not_existing_user_id)
        self.assertIsNone(user_object)


class ServiceUserDeleteUserByObjectTestCase(TestCase):

    def test_should_be_able_to_delete_user_by_object(self):
        """Should be able to delete user by object"""
        user_object = create_user_object()
        deleted_user_object = delete_user_by_object(user_object)
        self.assertEqual(user_object, deleted_user_object)


class ServiceUserCreateUserTestCase(TestCase):

    def test_should_be_able_create_user(self):
        """Should be able to create a user"""
        user_object = create_user(
            'root',
            'Super',
            'Admin',
            'root@old.st',
            '09106850351'
        )
        self.assertEqual({
            'username': 'root',
            'first_name': 'Super',
            'last_name': 'Admin',
            'email': 'root@old.st'
        }, {
            'username': user_object.username,
            'first_name': user_object.first_name,
            'last_name': user_object.last_name,
            'email': user_object.email,
        })


class ServiceUserUpdateUserTestCase(TestCase):

    def test_should_be_able_to_update_user(self):
        """Should be able to update a user"""
        user_object = create_user_object()
        update_user_object = update_user_by_object(
            user_object,
            'root2',
            'Super2',
            'Admin2',
            'root2@old.st',
            '09106850352'
        )
        self.assertEqual({
            'username': 'root2',
            'first_name': 'Super2',
            'last_name': 'Admin2',
            'email': 'root2@old.st'
        }, {
            'username': update_user_object.username,
            'first_name': update_user_object.first_name,
            'last_name': update_user_object.last_name,
            'email': update_user_object.email,
        })
