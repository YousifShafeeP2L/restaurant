from typing import Type, TypeVar

from pydantic import BaseModel
from tortoise.models import Model

T = TypeVar("T", bound=BaseModel)


async def partial_update(instance: Model, payload: BaseModel):
    item_data = payload.model_dump(exclude_defaults=True)
    for key, value in item_data.items():
        setattr(instance, key, value)
    await instance.save()


def convert_to_pydantic(
    instance: Model, schema: Type[T], special_fields: dict = {}
) -> T:
    try:
        item_dict = instance.__dict__
    except:
        item_dict = instance

    for key, value in special_fields.items():
        if key in schema.model_fields:
            item_dict[key] = value
    return schema.model_validate(item_dict)
