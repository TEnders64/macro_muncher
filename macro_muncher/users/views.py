from django.shortcuts import render, redirect
from django.views.generic import TemplateView, UpdateView
from .models import User, Profile
from .forms import LoginForm, RegistrationForm, UpdateUserForm, UpdateProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
class LoginView(TemplateView):
    template_name = 'users/login.html'
    form_class = LoginForm
    next_page = 'dashboard'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        form = self.form_class()
        if user is not None:
            print('valid user')
            login(request, user)
            return redirect(self.next_page)
        else:
            print('invalid credentials')
            return render(request, self.template_name, {'form':form})


class RegisterView(TemplateView):
    template_name = 'users/register.html'
    form_class = RegistrationForm
    next = 'dashboard'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            print('valid form')
            print(form.cleaned_data)
            data = form.cleaned_data
            user = User.objects.create_user(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                password=data['password1'],
            )
            return redirect(self.next)

        else:
            print('invalid form')
            print(form.cleaned_data)

        return render(request, self.template_name, {'form':form})

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'
    success_url = '/macros/dashboard'
    user_form = UpdateUserForm
    profile_form = UpdateProfileForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'user_form': self.user_form(instance=request.user), 'profile_form': self.profile_form(instance=request.user)})
