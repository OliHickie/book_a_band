from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages

from .models import Blog
from .forms import BlogForm


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


@user_passes_test(lambda u: u.is_superuser)
def add_blog(request):
    """
    A view to add a new band to the database
    """

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Blog successfully added')
            return redirect('all_blogs')
    else:
        form = BlogForm()

    return render(request, 'blogs/add_blog.html', {'form': form})
