from django.urls import path
from .views import about, booking, carlist, contact

urlpatterns = [
    path('about/', about, name='about'),
    path('booking/', booking, name='booking'),
    path('carlist/', carlist, name='carlist'),
    path('contact/', contact, name='contact')
]