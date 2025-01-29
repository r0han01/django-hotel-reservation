from django.urls import path
from .views import submit_reservation

urlpatterns = [
    path('reservation/', submit_reservation, name='submit_reservation'),
]
