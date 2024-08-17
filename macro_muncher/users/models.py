from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, first_name, last_name, email, password=None):
        if not first_name:
            raise ValueError('A first name is required.')
        if not last_name:
            raise ValueError('A last name is required.')
        if not email:
            raise ValueError('An email is required.')
        if not password:
            raise ValueError('A password is required.')
        email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name=last_name, email=email)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, first_name, last_name, email, password=None):
        if not first_name:
            raise ValueError('A first name is required.')
        if not last_name:
            raise ValueError('A last name is required.')
        if not email:
            raise ValueError('An email is required.')
        if not password:
            raise ValueError('A password is required.')
        user = self.create_user(first_name, last_name, email, password)
        user.is_superuser = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=45)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # for auth purposes, fulfilling the base class
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    objects = UserManager()

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    MALE = 'M'
    FEMALE = 'F'
    NO_ANSWER = 'N'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (NO_ANSWER, 'Prefer Not to Answer')
    ]

    gender = models.CharField(
        choices=GENDER_CHOICES,
        default=NO_ANSWER,
        max_length=20
    )
    date_of_birth = models.DateField(blank=True, null=True)
    height = models.IntegerField(default=60, null=True)

    # Activity-level Multiplier based on Mifflin-St.Jeor Equation
    INACTIVE = 1.2
    SLIGHTLY_ACTIVE = 1.375
    MODERATELY_ACTIVE = 1.55
    VERY_ACTIVE = 1.7
    EXTREMELY_ACTIVE = 1.9

    ACTIVITY_LEVEL_CHOICES = [
        (INACTIVE, 'Inactive/Sedentary'),
        (SLIGHTLY_ACTIVE, 'Slightly Active'),
        (MODERATELY_ACTIVE, 'Moderately Active'),
        (VERY_ACTIVE, 'Very Active'),
        (EXTREMELY_ACTIVE, 'Extremely Active'),
    ]

    activity_level = models.CharField(
        choices=ACTIVITY_LEVEL_CHOICES,
        default=INACTIVE,
        max_length=20
    )

    def __str__(self):
        return self.user.first_name+"'s Profile"