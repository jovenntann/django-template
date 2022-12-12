from django.test import TestCase

# Test Utilities from Account
from domain.users.tests.utils.utils import create_user_object

# Models
from ...models import Profile

import logging
logger = logging.getLogger(__name__)


# Create your tests here.
class ModelReceiverTestCase(TestCase):

    def test_should_create_profile_once_user_is_created(self):
        """Should create profile once user is created"""
        user_object = create_user_object()
        profile_object = Profile.objects.get(user=user_object)

        self.assertTrue(profile_object)
