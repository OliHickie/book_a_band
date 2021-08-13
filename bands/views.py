from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import BandForm


# Create your views here.
def add_band(request):

    if request.method == 'POST':
        form = BandForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = BandForm()
    return render(request, 'add_band.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')
