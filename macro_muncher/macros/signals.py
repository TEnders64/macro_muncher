from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import FoodItem

# this file helps prep a FoodItem instance for every new FoodItem that's saved to the db.
# it establishes the ratio of the portion size to the serving size
# and macros are then determined.

@receiver(pre_save, sender=FoodItem)
def save_food_item(sender, instance, **kwargs):
    print('FoodItem signals working!')
    print(instance)

    factor = instance.this_serving / instance.serving_size
    instance.proteins *= factor
    instance.fats *= factor
    instance.carbs *= factor
    print(instance.proteins, instance.fats, instance.carbs)