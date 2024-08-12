from django import forms
from .models import FoodItem, Measurement, Goal


class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name','serving_size','proteins','fats','carbs','this_serving']
        widgets = {
            'name': forms.TextInput(
                {'placeholder':'Food Name'}
            ),
            'serving_size': forms.NumberInput(
                {'placeholder':'Serving Size (g)', 'min': 0}
            ),
            'proteins': forms.NumberInput(
                {'placeholder':'Protein (g)', 'min': 0}
            ),
            'fats': forms.NumberInput(
                {'placeholder':'Fat (g)', 'min': 0}
            ),
            'carbs': forms.NumberInput(
                {'placeholder':'Carbs (g)', 'min': 0}
            ),
            'this_serving': forms.NumberInput(
                {'placeholder':'This Serving (g)', 'min': 0}
            ),
        }

class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = ['weight']
        widgets = {
            'weight': forms.NumberInput(
                {'min': 0, 'class': 'weight-input'}
            )
        }

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['goal_type', 'goal_pacing', 'goal_weight']
        widgets = {
            'goal_type': forms.Select(
                {'class': 'goal-type'}
            ),
            'goal_pacing': forms.Select(
                {'class': 'goal-pacing'}
            ),
            'goal_weight': forms.NumberInput(
                {'class': 'goal-weight', 'min': 0}
            ),
        }
