from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import FoodItemForm, MeasurementForm, GoalForm
from django.views.generic.edit import CreateView
from .models import User, FoodItem, Measurement, Goal
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime

# Create your views here.
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'macros/dashboard.html'

    def get_user(self):
        return User.objects.get(id=self.request.user.id)

    def get_context_data(self):
        # loading forms
        form_item = FoodItemForm()
        form_measurement = MeasurementForm()

        # using get_user helper function
        user = self.get_user()

        # getting latest goal and weight
        current_goal = user.goals.last()
        last_measurement = user.measurements.last()

        # handling food log for today's date
        food_log = FoodItem.objects.raw(f'SELECT * FROM macros_fooditem WHERE user_id = {user.id} AND DATE(created_at) = CURDATE();')


        consumed_calories = sum(food.total_calories() for food in food_log)
        consumed_protein = sum(food.proteins for food in food_log)
        consumed_fats = sum(food.fats for food in food_log)
        consumed_carbs = sum(food.carbs for food in food_log)

        return {
            'cals_max_value': 2140, # establish this
            'cals_this_value': consumed_calories,
            'cals_max_width': 100,
            'prot_max_value': 100, # establish this
            'prot_this_value': consumed_protein,
            'prot_max_width': 100,
            'fats_max_value': 90, # establish this
            'fats_this_value': consumed_fats,
            'fats_max_width': 100,
            'carbs_max_value': 300, # establish this
            'carbs_this_value': consumed_carbs,
            'carbs_max_width': 100,
            'current_goal': current_goal,
            'last_measurement': last_measurement,
            'form_item': form_item,
            'form_measurement': form_measurement,
            'food_log': food_log,

        }

class FoodItemCreateView(LoginRequiredMixin, CreateView):
    model = FoodItem
    fields = ['name','serving_size','proteins','fats','carbs','this_serving']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MeasurementCreateView(LoginRequiredMixin, CreateView):
    model = Measurement
    fields = ['weight']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class GoalUpdateView(LoginRequiredMixin, CreateView):
    template_name = 'macros/change-goals.html'
    form_class = GoalForm
    success_url = '/macros/dashboard'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
