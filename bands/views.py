from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BandForm

from .models import Band


def all_bands(request):
    """
    A view to display all bands
    """
    # Display bands, ordered by rating (highest first)
    bands = Band.objects.all().order_by('-rating')

    return render(request, 'bands/bands.html', {'bands': bands})


def band_profile(request, band_id):
    """
    A view to display the band profile
    """

    band = get_object_or_404(Band, pk=band_id)

    # Return four random bands in same category, excluding current band
    random_bands = Band.objects.all().filter(
        category=band.category).exclude(pk=band_id).order_by('?')[:4]

    context = {
        'band': band,
        'random_bands': random_bands,
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
    return render(request, 'bands/add_band.html', {'form': form})


# remove once messages complete
def success(request):
    return HttpResponse('successfully uploaded')
