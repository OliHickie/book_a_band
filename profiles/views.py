from django.shortcuts import render


def profile(request):
    """
    A view to display users profile
    """

    context = {

    }

    return render(request, 'profiles/profile.html', context)
