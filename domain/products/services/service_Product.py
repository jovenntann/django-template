from django.utils import timezone
from typing import List

# Models
from ..models import Product, Category
from domain.stores.models import Store

import logging
logger = logging.getLogger(__name__)


def get_products() -> List[Product]:
    product_objects = Product.objects.all().prefetch_related('categories')
    logger.info(f"{product_objects} fetched")
    return product_objects


def get_product_by_id(product_id: int) -> Product:
    product_object = Product.objects.filter(id=product_id).first()
    logger.info(f"{product_object} fetched")
    return product_object


def delete_product_by_object(product_object: Product) -> Product:
    product_object.delete()
    logger.info(f"{product_object} has been deleted.")
    return product_object


def create_product(
        store_object: Store,
        categories: List[Category],
        title: str,
        description: str
) -> Product:

    product_object = Product.objects.create(
        store=store_object,
        title=title,
        description=description
    )
    product_object.categories.set(categories)
    # NOTE: This is nice because this instance won't save if the categories.set failed :)
    product_object.save()

    logger.info(f"\"{product_object.title}\" has been created")

    return product_object


def update_product_by_object(
        product_object: Product,
        store_object: Store,
        categories: List[Category],
        title: str,
        description: str
) -> Product:
    product_object.store = store_object
    product_object.title = title
    product_object.description = description
    product_object.updated_at = timezone.now()

    if type(categories) == list:
        product_object.categories.set(categories)

    product_object.save()

    logger.info(f"\"{product_object}\" has been updated.")

    return product_object
