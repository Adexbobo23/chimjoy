from django.urls import path
from .views import AdminUserRegistrationView

urlpatterns = [
    path('reg/', AdminUserRegistrationView.as_view(), name='adminreg'),
]