from typing import Optional

from pydantic import BaseModel
from tortoise import fields, models


class Restaurant(models.Model):
    title = fields.CharField(max_length=40)
    description = fields.CharField(max_length=40, null=True)
    image = fields.CharField(max_length=40, null=True)
    rating = fields.FloatField()

    class Meta:
        table = "restaurant"


class BaseRestaurant(BaseModel):
    title: str
    description: Optional[str] = None
    image: Optional[str] = None
    rating: float


class RestaurantSchema(BaseRestaurant):
    id: int
