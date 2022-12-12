from django.test import TestCase

# Test Utilities from Account
from domain.users.tests.utils.utils import create_user_object

# Models
from ...models import Profile

import logging
logger = logging.getLogger(__name__)


# Create your tests here.
class ModelProfileTestCase(TestCase):

    def should_be_able_to_create_profile(self):
        user_object = create_user_object()

        profile_object = Profile.objects.create(
            user=user_object,
            bio="Biography",
            location="Manila",
            birth_date="1990-01-01"
        )

        self.assertEqual({
            'bio': 'Biography',
            'location': 'Manila',
            'birth_date': '1990-01-01'
        }, {
            'bio': profile_object.bio,
            'location': profile_object.location,
            'birth_date': profile_object.birth_date
        })
