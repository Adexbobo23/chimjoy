from django.urls import path
from .views import ( CustomUserAuthenticationView, custom_logout, dashboard
)

urlpatterns = [
    path('authentication/', CustomUserAuthenticationView.as_view(), name='authentication'),
    path('logout/', custom_logout, name='logout'),
    path('home/', dashboard, name='dashboard'),
]
