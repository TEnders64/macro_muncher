from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import FoodItemForm, MeasurementForm, GoalForm
from django.views.generic.edit import CreateView
from .models import FoodItem, Measurement, Goal
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'macros/dashboard.html'

    def get_context_data(self):
        form_item = FoodItemForm()
        form_measurement = MeasurementForm()
        current_goal = Goal.objects.filter(user=self.request.user).last()
        last_measurement = Measurement.objects.filter(user=self.request.user).last()
        food_log = FoodItem.objects.filter(user=self.request.user)

        return {
            'cals_max_value': 2140,
            'cals_this_value': 921,
            'cals_max_width': 100,
            'prot_max_value': 100,
            'prot_this_value': 56,
            'prot_max_width': 100,
            'fats_max_value': 90,
            'fats_this_value': 25,
            'fats_max_width': 100,
            'carbs_max_value': 300,
            'carbs_this_value': 118,
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
