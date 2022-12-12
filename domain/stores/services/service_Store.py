from django.utils import timezone
from typing import List

# Models
from django.contrib.auth.models import User
from ..models import Store

import logging
logger = logging.getLogger(__name__)


def get_stores() -> List[Store]:
    store_objects = Store.objects.all()
    logger.info(f"{store_objects} fetched")
    return store_objects


def create_store(
        user_object: User,
        name: str,
        contact_number: str,
        address: str
) -> Store:
    store_object = Store.objects.create(
        user=user_object,
        name=name,
        contact_number=contact_number,
        address=address
    )
    store_object.save()
    logger.info(f"\"{store_object}\" has been created")
    return store_object


def get_store_by_id(store_id: int) -> Store:
    store_object = Store.objects.filter(id=store_id).first()
    if store_object:
        logger.info(f"{store_object} fetched")
        return store_object
    return store_object


def delete_store_by_object(store_object: Store) -> Store:
    store_object.delete()
    logger.info(f"{store_object} has been deleted.")
    return store_object


def update_store_by_object(
        store_object: Store,
        user_object: User,
        name: str,
        contact_number: str,
        address: str
) -> Store:
    store_object.store = store_object
    store_object.user = user_object
    store_object.name = name
    store_object.contact_number = contact_number
    store_object.address = address
    store_object.updated_at = timezone.now()

    store_object.save()

    logger.info(f"\"{store_object}\" has been updated.")

    return store_object
