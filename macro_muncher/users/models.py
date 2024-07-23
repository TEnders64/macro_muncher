from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    MALE = 'M'
    FEMALE = 'F'
    NO_ANSWER = 'N'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (NO_ANSWER, 'Prefer Not to Answer')
    ]

    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField(max_length=254)
    username = models.CharField(max_length=45, unique=True)
    date_of_birth = models.DateField(blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES,
        default=NO_ANSWER,
        max_length=20
    )
    address = models.TextField

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

