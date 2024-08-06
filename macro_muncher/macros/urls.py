from django.urls import path
from .views import DashboardView, FoodItemCreateView

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('foods/', FoodItemCreateView.as_view(), name='food_item'),
]