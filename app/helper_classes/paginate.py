from typing import Generic, List, Optional, Type, TypeVar

from app.const.enum import DEFAULT_PAGE, DEFAULT_PAGE_SIZE
from app.helper_classes.model_utils import convert_to_pydantic
from app.helper_classes.request_utils import get_param
from fastapi import Request
from pydantic import BaseModel
from tortoise.models import Model

T = TypeVar("T", bound=BaseModel)


class PaginatedResponse(BaseModel, Generic[T]):
    data: List[T]
    total: int
    page: int
    pages: int
    next_page: Optional[int]
    prev_page: Optional[int]
    next_page_url: Optional[str]
    prev_page_url: Optional[str]


async def paginate(
    request: Request, all_items: List[Model], model: Type[T] = None
) -> PaginatedResponse[T]:
    """
    Args:
        model (BaseModel, optional): Pydantic model to convert ORM to Pydantic. Defaults to None.
    """
    page = get_param(request, "page", int, DEFAULT_PAGE)
    size = get_param(request, "size", int, DEFAULT_PAGE_SIZE)
    offset = (page - 1) * size
    total = len(all_items)
    data = all_items[offset : offset + size]
    if model:
        data = [convert_to_pydantic(item, model) for item in data]
    total_pages = (total + size - 1) // size

    next_page = page + 1 if page < total_pages else None
    prev_page = page - 1 if page > 1 else None
    next_page_url = (
        str(request.url.include_query_params(page=next_page)) if next_page else None
    )
    prev_page_url = (
        str(request.url.include_query_params(page=prev_page)) if prev_page else None
    )

    return PaginatedResponse[T](
        data=data,
        total=total,
        pages=total_pages,
        page=page,
        next_page=next_page,
        prev_page=prev_page,
        next_page_url=next_page_url,
        prev_page_url=prev_page_url,
    )
