from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User  
from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomUserRegistrationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CustomUserLoginForm 
from django.contrib.auth import logout
from application.models import Vehicle 
from django.contrib.auth.decorators import login_required



class CustomUserAuthenticationView(View):
    template_name = 'index.html'

    def get(self, request):
        login_form = CustomUserLoginForm()
        registration_form = CustomUserRegistrationForm()
        return render(request, self.template_name, {
            'login_form': login_form,
            'registration_form': registration_form,
        })

    def post(self, request):
        if 'login_submit' in request.POST:
            # Handle login form submission
            login_form = CustomUserLoginForm(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']

                # Authenticate the user using the provided credentials with your custom user model
                user = authenticate(request, username=username, password=password)

                if user is not None:
                    # Login the authenticated user
                    login(request, user)
                    messages.success(request, 'Login successful.')
                    return redirect('dashboard')
                else:
                    messages.error(request, 'Invalid login credentials. Please try again.')
            registration_form = CustomUserRegistrationForm()

        elif 'registration_submit' in request.POST:
            # Handle registration form submission
            registration_form = CustomUserRegistrationForm(request.POST)
            if registration_form.is_valid():
                # Form data is valid, create a new user
                username = registration_form.cleaned_data['username']
                email = registration_form.cleaned_data['email']
                password = registration_form.cleaned_data['password']
                confirm_password = registration_form.cleaned_data['confirm_password']

                if password != confirm_password:
                    registration_form.add_error('confirm_password', 'Passwords do not match')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        login(request, user)
                        messages.success(request, 'Registration successful.')
                        return redirect('dashboard')
                    else:
                        return redirect('login')
            login_form = CustomUserLoginForm()
            
        else:
            login_form = CustomUserLoginForm()
            registration_form = CustomUserRegistrationForm()

        return render(request, self.template_name, {
            'login_form': login_form,
            'registration_form': registration_form,
        })
    

def custom_logout(request):
    logout(request) 
    return redirect('authentication')


@login_required(login_url='authentication')
def dashboard(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'dashboard.html', {'vehicles': vehicles})