from django.utils import timezone
from typing import List

# Models
from ..models import Category

import logging
logger = logging.getLogger(__name__)


def get_categories() -> List[Category]:
    category_objects = Category.objects.all()
    logger.info(f"{category_objects} fetched")
    return category_objects


def get_category_by_id(category_id: int) -> Category:
    category_object = Category.objects.filter(id=category_id).first()
    logger.info(f"{category_object} fetched")
    return category_object


def delete_category_by_object(category_object: Category) -> Category:
    category_object.delete()
    logger.info(f"{category_object} has been deleted.")
    return category_object


def create_category(name: str, description: str) -> Category:
    category_object = Category.objects.create(
        name=name,
        description=description
    )
    category_object.save()
    logger.info(f"\"{category_object}\" has been created")
    return category_object


def update_category_by_object(
        category_object: Category,
        name: str,
        description: str
) -> Category:
    category_object.name = name
    category_object.description = description
    category_object.updated_at = timezone.now()

    category_object.save()
    logger.info(f"\"{category_object}\" has been updated")

    return category_object
