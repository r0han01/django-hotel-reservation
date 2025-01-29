from django.db import models

class HotelReservation(models.Model):
    # Guest Detail
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    country = models.CharField(max_length=50, default="US")
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    company = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()

    # Account Detail
    payment_type = models.CharField(max_length=20, choices=[('CA', 'Cash'), ('CHECK', 'Check'), ('CREDIT CARD', 'Credit Card')])

    # Room/Stay Detail
    arrival_date = models.DateField()
    departure_date = models.DateField()
    number_of_nights = models.IntegerField(default=1)
    number_of_rooms = models.IntegerField(default=1)
    room_type = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    arrival_time = models.TimeField()
    departure_time = models.TimeField(default="11:00:00")
    confirmation_code = models.CharField(max_length=50)
    requested_room = models.CharField(max_length=100)
    room_number = models.CharField(max_length=10)

    def __str__(self):
        return f"Reservation for {self.first_name} {self.last_name}"
