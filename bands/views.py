from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib import messages

from .forms import BandForm, ReviewForm
from .models import Band, Category, BandReview


def all_bands(request):
    """
    A view to display all bands and quick links
    """
    bands = Band.objects.all().order_by('name')
    number_of_bands = len(bands)
    categories = Category.objects.all()
    query = None

    # full list of locations
    full_location_list = []
    # location list without duplicates
    locations = []
    for band in bands:
        i = band.location
        full_location_list.append(i)
        if i not in locations:
            locations.append(i)

    # sorted alphabetically
    sorted_locations = sorted(locations)

    # Count number of occurances for each location, add to dict
    locations_counted = {}
    for x in sorted_locations:
        num = full_location_list.count(x)
        locations_counted[x] = num

    # Search for bands
    if request.GET:
        if 'category' in request.GET:
            category = request.GET['category']
            bands = bands.filter(category__name=category)

        if 'sort' in request.GET:
            sortby = request.GET['sort']
            bands = Band.objects.all().order_by(sortby)
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    bands = bands.order_by("-" + sortby)

        if 'q' in request.GET:
            query = request.GET['q']
            queries = Q(name__icontains=query) | Q(biography__icontains=query)
            bands = bands.filter(queries)

        # Search by location
        if 'locations' in request.GET:
            query = request.GET['locations']
            queries = Q(location__icontains=query)
            bands = bands.filter(queries)

        # Search by group
        if 'group' in request.GET:
            query = request.GET['group']
            bands = bands.filter(category__name=query)

        # Search by price
        if 'price' in request.GET:
            query = request.GET['price']
            if query == '£2000':
                bands = bands.filter(price__gte=2000)
            if query == '£1500':
                bands = bands.filter(price__range=(1500, 1999))
            if query == '£1000':
                bands = bands.filter(price__range=(1000, 1499))
            if query == '£500':
                bands = bands.filter(price__range=(500, 999))
            if query == 'Less than £500':
                bands = bands.filter(price__lt=500)

    # Pagination
    paginator = Paginator(bands, 9)

    page_number = request.GET.get('page')
    page_bands = paginator.get_page(page_number)

    context = {
        'bands': bands,
        'number_of_bands': number_of_bands,
        'categories': categories,
        'locations': locations,
        'locations_counted': locations_counted,
        'query': query,
        'page_bands': page_bands,
    }

    return render(request, 'bands/bands.html', context)


def band_profile(request, band_id):
    """
    A view to display the band profile, add reviews and suggest similar artists
    """
    band = get_object_or_404(Band, pk=band_id)
    # Get band reviews in date order
    reviews = BandReview.objects.filter(band=band_id).order_by('-date_added')

    # Find average rating and round to 1 decimal place
    average_rating = None
    if reviews:
        ratings = []
        for review in reviews:
            ratings.append(review.rating)

        average_rating = round(sum(ratings)/len(ratings), 1)

    # Return four random bands in same category, excluding current band
    random_bands = Band.objects.all().filter(
        category=band.category).exclude(pk=band_id).order_by('?')[:4]

    context = {
        'band': band,
        'random_bands': random_bands,
        'reviews': reviews,
        'average_rating': average_rating,
    }

    return render(request, 'bands/band_profile.html', context)


@user_passes_test(lambda u: u.is_superuser)
def add_band(request):
    """
    A view to add a new band to the database
    """

    if request.method == 'POST':
        form = BandForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'The band has been successfully added')

        return redirect(reverse('all_bands'))

    else:
        form = BandForm()

    return render(request, 'bands/add_band.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def edit_band(request, band_id):
    """
    A view to edit band details
    """
    band = get_object_or_404(Band, pk=band_id)

    if request.method == 'POST':
        form = BandForm(request.POST, request.FILES, instance=band)
        if form.is_valid():
            form.save()
            messages.success(request, 'The band has been successfully updated')

        return redirect(reverse('band_profile', kwargs={'band_id': band_id}))

    else:
        form = BandForm(instance=band)

    context = {
        'form': form,
        'band': band,
    }

    return render(request, 'bands/edit_band.html', context)


@login_required
def add_review(request, band_id):
    """
    Add a review for a band
    """
    band = get_object_or_404(Band, pk=band_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.band = band
            review.save()
            messages.success(
                request, 'Your review has been successfully added.')

        return redirect(reverse('band_profile', kwargs={'band_id': band_id}))

    else:
        form = ReviewForm()

    context = {
        'form': form,
        'band': band,
    }

    return render(request, 'bands/add_review.html', context)
