from django import forms
from .models import RideBooking, Vehicle

# List of states in Nigeria
nigerian_states = [
    "Abia", "Adamawa", "Akwa Ibom", "Anambra", "Bauchi", "Bayelsa", "Benue",
    "Borno", "Cross River", "Delta", "Ebonyi", "Edo", "Ekiti", "Enugu", "FCT",
    "Gombe", "Imo", "Jigawa", "Kaduna", "Kano", "Katsina", "Kebbi", "Kogi",
    "Kwara", "Lagos", "Nasarawa", "Niger", "Ogun", "Ondo", "Osun", "Oyo",
    "Plateau", "Rivers", "Sokoto", "Taraba", "Yobe", "Zamfara"
]

class RideBookingForm(forms.ModelForm):
    pickup_location = forms.ChoiceField(choices=[(state, state) for state in nigerian_states])
    destination = forms.ChoiceField(choices=[(state, state) for state in nigerian_states])
    model = forms.ModelChoiceField(queryset=Vehicle.objects.all(), empty_label="Select a vehicle")

    class Meta:
        model = RideBooking
        fields = ['model','pickup_location', 'destination', 'date', 'time', 'email', 'phone_number']

    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
    )

    time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
    )
