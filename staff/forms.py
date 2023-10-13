from django import forms
from .models import AdminUser

class AdminUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = AdminUser
        fields = ['username', 'email', 'password']

class AdminUserChangeForm(forms.ModelForm):
    class Meta:
        model = AdminUser
        fields = ['username', 'email']
