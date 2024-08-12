from django.db import models
from users.models import User
from django.conf import settings
from django.urls import reverse

# Create your models here.
class FoodItem(models.Model):
    name = models.CharField(max_length=45, db_column='food_name')
    serving_size = models.IntegerField()
    proteins = models.IntegerField()
    fats = models.IntegerField()
    carbs = models.IntegerField()
    this_serving = models.IntegerField()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("dashboard")


class Goal(models.Model):
    LOSE_WEIGHT = 'Lose'
    MAINTAIN = 'Maintain'
    GAIN_WEIGHT = 'Gain'
    GOAL_CHOICES = [
        (LOSE_WEIGHT, 'Lose Weight'),
        (MAINTAIN, 'Maintain'),
        (GAIN_WEIGHT, 'Gain Weight')
    ]

    goal_type = models.CharField(
        choices=GOAL_CHOICES,
        default=None,
        max_length=12
    )

    SLOW = 'Slow'
    RECOMMENDED = 'Recommended'
    FAST = 'Aggressive'
    PACE_CHOICES = [
        (SLOW, 'Slow'),
        (RECOMMENDED, 'Recommended'),
        (FAST, 'Aggressive')
    ]

    goal_pacing = models.CharField(
        choices=PACE_CHOICES,
        default=None,
        max_length=12
    )

    goal_weight = models.IntegerField()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Measurement(models.Model):
    weight = models.IntegerField()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)