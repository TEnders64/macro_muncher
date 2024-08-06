from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import FoodItemForm
from django.views.generic.edit import CreateView
from .models import FoodItem

# Create your views here.
class DashboardView(TemplateView):
    template_name = 'macros/dashboard.html'

    def get_context_data(self, **kwargs):
        form = FoodItemForm()
        return {
            'goal_type': 'Lose Weight',
            'goal_weight': 150,
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
            'form': form,
        }

class FoodItemCreateView(CreateView):
    model = FoodItem