from django.contrib import admin
from .models import FoodItem, Goal, Measurement

admin.site.register(FoodItem, admin.ModelAdmin)
admin.site.register(Goal, admin.ModelAdmin)
admin.site.register(Measurement, admin.ModelAdmin)