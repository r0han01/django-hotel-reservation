from django.shortcuts import render, redirect
from .forms import HotelReservationForm

def submit_reservation(request):
    if request.method == 'POST':
        form = HotelReservationForm(request.POST)
        if form.is_valid():
            form.save()
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            
            # Optional: You can add a success message to show to the user.
            # Redirect to the reservation form after 10 seconds
            return redirect('submit_reservation')  # This redirects to the reservation page

    else:
        form = HotelReservationForm()

    return render(request, 'userform/reservation_form.html', {'form': form})
