from django import forms
from .models import HotelReservation

class HotelReservationForm(forms.ModelForm):
    class Meta:
        model = HotelReservation
        fields = [
            'last_name', 'first_name', 'country', 'address', 'city', 'state', 'postal_code',
            'phone_number', 'company', 'email', 'payment_type', 'arrival_date', 'departure_date',
            'number_of_nights', 'number_of_rooms', 'room_type', 'rate', 'arrival_time', 'departure_time',
            'confirmation_code', 'requested_room', 'room_number'
        ]
