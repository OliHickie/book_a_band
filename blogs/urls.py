from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.read_blog, name='read_blog'),
    path('add_blog/', views.add_blog, name='add_blog'),
]
