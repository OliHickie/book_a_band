from django.shortcuts import render, get_object_or_404

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


def read_blog(request, blog_id):
    """
    A view to display blog content
    """

    blog = get_object_or_404(Blog, pk=blog_id)

    context = {
        'blog': blog,
    }

    return render(request, 'blogs/read-blog.html', context)
