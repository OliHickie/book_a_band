from django.urls import path
from . import views

urlpatterns = [
    path('new_booking/<int:band_id>/', views.new_booking, name='new_booking'),
    path('my_bookings', views.my_bookings, name='my_bookings'),
]
