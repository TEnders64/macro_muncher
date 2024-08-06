from django.forms import ModelForm
from .models import FoodItem


class FoodItemForm(ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name','serving_size','proteins','fats','carbs','this_serving','user']