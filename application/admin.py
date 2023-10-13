from django.contrib import admin
from .models import RideBooking, Vehicle

# Register your models here.
admin.site.register(RideBooking)
admin.site.register(Vehicle)