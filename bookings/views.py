from django.shortcuts import render, get_object_or_404

from bands.models import Band


def new_booking(request, band_id):
    """
    A view to display booking form
    """
    band = get_object_or_404(Band, pk=band_id)

    return render(request, 'bookings/new_booking.html', {'band': band})
