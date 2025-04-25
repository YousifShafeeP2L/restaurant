from django.urls import path
from .views import RestaurantView, RestaurantDetailView

app_name = "main"

urlpatterns = [
    path("restaurant/", RestaurantView.as_view()),
    path("restaurant/<int:pk>/", RestaurantDetailView.as_view()),
]
