from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BandForm

from .models import Band


def all_bands(request):
    """
    A view to display all bands
    """

    bands = Band.objects.all()

    return render(request, 'bands/bands.html', {'bands': bands})


def band_profile(request, band_id):
    """ A view to display the band profile """

    band = get_object_or_404(Band, pk=band_id)

    context = {
        'band': band,
    }

    return render(request, 'bands/band_profile.html', context)


def add_band(request):
    """
    A view to add a new band to the database
    """

    if request.method == 'POST':
        form = BandForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            # change to form when messages complete
            return redirect('success')
    else:
        form = BandForm()
    return render(request, 'add_band.html', {'form': form})


# remove once messages complete
def success(request):
    return HttpResponse('successfully uploaded')
