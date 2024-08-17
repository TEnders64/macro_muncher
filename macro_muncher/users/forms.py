from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User, Profile

# Corresponding Login, Register, and Profile forms below
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['email','password']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'me@example.com'}),
        }

class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(
                {'placeholder':'First Name'}
            ),
            'last_name': forms.TextInput(
                {'placeholder':'Last Name'}
            ),
            'email': forms.EmailInput(
                {'placeholder':'me@example.com'}
            ),
        }

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['gender', 'date_of_birth', 'height', 'activity_level']