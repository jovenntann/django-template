from .Profile import Profile

from django.contrib.auth.models import User

# Method: Extending User with Profile
from django.db.models.signals import post_save
from django.dispatch import receiver

# Celery: Tasks
from ..tasks.task_mailer import send_email_verification

import logging
logger = logging.getLogger(__name__)


# Method: Extending User with Profile
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        logger.info("@receiver.created -> create_user_profile")
        Profile.objects.create(user=instance)
        logger.info(f"create profile for username: {instance.username}")
        send_email_verification.delay(instance.email, 'Please verify your email')
        logger.info("task created: send_email_verification")


# Method: Extending User with Profile
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    logger.info("@receiver.post_save -> save_user_profile")
    instance.profile.save()
    logger.info(f"profile has been created for username: {instance.username}")

