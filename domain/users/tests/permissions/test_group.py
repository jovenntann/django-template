from django.test import TestCase

# Utils
from ..utils.utils import create_user_object, create_admin_user_object

# Permissions
from ...permissions.permission_group import is_in_group, has_group_permission
from ...permissions.permission_group import IsAdminUser

import logging
logger = logging.getLogger(__name__)


# Create your tests here.
class PermissionsGroupIsInGroupTestCase(TestCase):

    def test_should_return_false_if_user_is_in_specific_groups(self):
        """Should return False if user is not in specific Groups"""
        user_object = create_user_object()
        _is_in_group = is_in_group(user_object, 'admin')
        self.assertFalse(_is_in_group)

    def test_should_return_true_if_user_is_in_specific_groups(self):
        """Should return True if user is in specific Groups"""
        user_object = create_admin_user_object()
        _is_in_group = is_in_group(user_object, 'admin')
        self.assertTrue(_is_in_group)


class PermissionsGroupHasGroupPermissionTestCase(TestCase):

    def test_should_return_none_if_user_not_in_group(self):
        """Should return None if the user if not in group"""
        user_object = create_user_object()
        _has_group_permission = has_group_permission(user_object, 'admin')
        self.assertFalse(_has_group_permission)

    def test_should_return_group_objects_if_user_is_in_group(self):
        """Should return Group Objects if the user is in group"""
        user_object = create_admin_user_object()
        _has_group_permission = has_group_permission(user_object, 'admin')
        self.assertIsNotNone(_has_group_permission)


# TODO: Find a way to test this
# class PermissionsGroupIsAdminUserTestCase(TestCase):
#
#     def test_should_return_false_if_user_is_not_in_admin_group(self):
#         """Should return False of the user is not in Admin group"""
#         user_object = create_admin_user_object()
#         is_admin_user = IsAdminUser.has_permission(user_object, request=None, view=None)
#         self.assertFalse(is_admin_user)
#
#     def test_should_return_true_if_user_is_admin(self):
#         """Should return True of the user is in Admin group"""
#         user_object = create_admin_user_object()
#         is_admin_user = IsAdminUser.has_permission(user_object, request=None, view=None)
#         self.assertTrue(is_admin_user)

