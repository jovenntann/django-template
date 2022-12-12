# Tests
from django.test import TestCase
from rest_framework.test import APIClient

# Models
from domain.users.models import Profile

# Test Utilities from Account
from domain.users.tests.utils.utils import create_user_object, generate_token

import json
import logging

logger = logging.getLogger(__name__)


class UserAPIViewTestCase(TestCase):

    def test_authenticated_user_should_get_user_data(self):
        """Authenticated User should get its own user data"""
        user_object = create_user_object()
        access_token = generate_token()

        # Update Profile Data (Since it's already created from signals)
        profile_object = Profile.objects.get(user=user_object)
        profile_object.bio = "Biography"
        profile_object.location = "Manila"
        profile_object.birth_date = "1990-01-01"
        profile_object.save()

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        path = "/authenticated/user"
        response = client.get(path)
        content = json.loads(response.content)

        self.assertEqual({
            'id': user_object.pk,
            'username': 'root',
            'first_name': 'Super',
            'last_name': 'Admin',
            'email': 'root@old.st'
        }, content)
