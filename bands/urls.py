from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_bands, name='all_bands'),
    path('add_band/', views.add_band, name='add_band'),
    path('success/', views.success, name='success'),
]
