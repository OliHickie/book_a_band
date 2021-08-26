from django.shortcuts import render

from .models import Blog


def all_blogs(request):
    """
    A view to display all bog posts
    """
    blogs = Blog.objects.all().order_by('updated_at')

    context = {
        'blogs': blogs,
    }

    return render(request, 'blogs/blogs.html', context)
