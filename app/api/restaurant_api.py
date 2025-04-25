from app.helper_classes.exception_handler import CustomError
from app.helper_classes.paginate import paginate
from app.models.restaurant import RestaurantSchema, BaseRestaurant
from fastapi import APIRouter, Request
from app.models.restaurant import Restaurant
from app.helper_classes.model_utils import partial_update

router = APIRouter(prefix="/restaurant")


@router.get("/")
async def get_restaurants(request: Request):
    restaurants = await Restaurant.all()
    return await paginate(request, restaurants, RestaurantSchema)


@router.post("/")
async def create_restaurant(payload: BaseRestaurant):
    restaurant = await Restaurant.create(**payload.model_dump())
    return restaurant


@router.patch("/{id}/")
async def update_restaurant(id: int, payload: BaseRestaurant):
    restaurant = await Restaurant.get(id=id)
    if not restaurant:
        raise CustomError("Restaurant not found")
    await partial_update(restaurant, payload)
    return restaurant


@router.delete("/{id}/")
async def delete_restaurant(id: int):
    restaurant = await Restaurant.get(id=id)
    if not restaurant:
        raise CustomError("Restaurant not found")
    await restaurant.delete()
    return {"message": "Restaurant deleted successfully"}
