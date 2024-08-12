from django.urls import path
from .views import DashboardView, FoodItemCreateView, MeasurementCreateView, GoalUpdateView

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('foods/', FoodItemCreateView.as_view(), name='food_item'),
    path('measurement/', MeasurementCreateView.as_view(), name='measurement'),
    path('goals/', GoalUpdateView.as_view(), name='goals'),
]