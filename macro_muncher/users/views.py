from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import User
from .forms import LoginForm, RegistrationForm

# Create your views here.
class LoginView(TemplateView):
    template_name = 'users/login.html'
    form_class = LoginForm
    next = 'dashboard'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            print('valid form')
        else:
            print('invalid form')
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
