from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
import datetime
import stripe

from .forms import BookingForm
from .models import NewBooking
from bands.models import Band


@login_required
def new_booking(request, band_id):
    """
    A view to display booking form and process booking
    """
    band = get_object_or_404(Band, pk=band_id)
    form = BookingForm()

    if request.method == 'POST':

        date_input = request.POST['wedding_date']
        wedding_date = datetime.datetime.strptime(date_input, "%d-%m-%Y").strftime("%Y-%m-%d")

        booking_form = {
            'client_name': request.POST['client_name'],
            'contact_number': request.POST['contact_number'],
            'venue_name': request.POST['venue_name'],
            'venue_address1': request.POST['venue_address1'],
            'venue_address2': request.POST['venue_address2'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'wedding_date': wedding_date,
            'start_time': request.POST['start_time'],
            'emergency_contact': request.POST['emergency_contact'],
            'emergency_phone': request.POST['emergency_phone'],
            'additional_information': request.POST['additional_information'],
        }

        form = BookingForm(booking_form)
        if form.is_valid():
            booking_form = form.save(commit=False)
            booking_form.email = request.user.email
            booking_form.band_name = band.name
            booking_form.price = band.price
            form.save()

        return redirect('my_bookings')

    context = {
            'band': band,
            'form': form,
            }

    return render(request, 'bookings/new_booking.html', context)


@login_required
def my_bookings(request):
    """
    A view to display users bookings
    """
    user = request.user.email
    bookings = NewBooking.objects.filter(email=user).order_by('paid')

    confirmed_bookings = bookings.filter(paid=True)
    unconfirmed_bookings = bookings.filter(paid=False)
    total = 0
    for booking in unconfirmed_bookings:
        total += booking.price

    request.session['balance'] = total

    context = {
        'bookings': bookings,
        'user': user,
        'confirmed_bookings': confirmed_bookings,
        'unconfirmed_bookings': unconfirmed_bookings,
    }

    return render(request, 'bookings/my_bookings.html', context)


def payments(request):
    """
    A view to handle Stripe payments
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    
    user = request.user.email
    unconfirmed_bookings = NewBooking.objects.filter(email=user, paid=False)

    if request.method == 'POST':
        # If payment is successful, change all bookings to CONFIRMED
        unconfirmed_bookings.update(paid=True)

        return redirect(reverse('my_bookings'))

    else:
        balance = request.session['balance']
        stripe_balance = int(balance * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_balance,
            currency=settings.STRIPE_CURRENCY,
        )

    context = {
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'stripe_balance': stripe_balance,
        'balance': balance,
        'unconfirmed_bookings': unconfirmed_bookings,
    }

    return render(request, 'bookings/payments.html', context)
