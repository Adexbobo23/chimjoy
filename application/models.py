from django.db import models
from django.contrib.auth.models import User

class RideBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.CharField(max_length=100, default='select car model')
    pickup_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    
    # Add email and phone number fields
    email = models.CharField(max_length=255, default='Your Email here')  # Email field
    phone_number = models.CharField(max_length=15, default='Your phone number')  # Phone number field

    def __str__(self):
        return f"Ride from {self.pickup_location} to {self.destination} on {self.date} at {self.time}"


class Vehicle(models.Model):
    # Vehicle details
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=15)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    
    # Vehicle type (e.g., Sedan, SUV, Truck, etc.)
    vehicle_type = models.CharField(max_length=50)
    
    # Maximum passenger capacity
    passenger_capacity = models.PositiveSmallIntegerField()
    
    # Cargo capacity (if applicable)
    cargo_capacity = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    # Fuel type (e.g., Gasoline, Diesel, Electric)
    fuel_type = models.CharField(max_length=50)
    
    # Vehicle registration and insurance details
    registration_number = models.CharField(max_length=50)
    
    # Image field for vehicle picture
    picture = models.ImageField(upload_to='vehicles/')
    
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
