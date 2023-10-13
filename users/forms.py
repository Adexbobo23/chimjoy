from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomUserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)


class CustomUserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
