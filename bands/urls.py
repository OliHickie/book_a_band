from django.urls import path
from . import views

urlpatterns = [
    path('add_band/', views.add_band, name='add_band'),
    path('success/', views.success, name='success'),
]
