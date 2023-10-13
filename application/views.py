from django.shortcuts import render, redirect
from .forms import RideBookingForm
from .models import Vehicle
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages


@login_required(login_url='authentication')
def about(request):
    return render(request, 'about.html')


# Your existing imports for forms, models, etc.

@login_required(login_url='authentication')
def booking(request):
    if request.method == 'POST':
        form = RideBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, 'Booking successful!')  # Add a success message

            # Send an email notification to the admin
            subject = 'New Booking Notification'
            message = f'A new booking has been made by {request.user.username}.\n\n'
            message += f'Pickup Location: {booking.pickup_location}\n'
            message += f'Destination: {booking.destination}\n'
            message += f'Model: {booking.model}\n'
            message += f'Date: {booking.date}\n'
            message += f'Time: {booking.time}\n'
            message += f'Email: {booking.email}\n'
            message += f'Phone Number: {booking.phone_number}\n'

            from_email = 'admin@chimjoylogistics.com.ng'  # Replace with your app's email
            recipient_list = ['admin@chimjoylogistics.com.ng']

            send_mail(subject, message, from_email, recipient_list, fail_silently=True)

            return redirect('booking')
    else:
        form = RideBookingForm()
    
    return render(request, 'booking.html', {'form': form})


@login_required(login_url='authentication')
def carlist(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'carlist.html', {'vehicles': vehicles})


@login_required(login_url='authentication')
def contact(request):
    return render(request, 'contact.html')