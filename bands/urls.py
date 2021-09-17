from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_bands, name='all_bands'),
    path('<int:band_id>/', views.band_profile, name='band_profile'),
    path('add_band/', views.add_band, name='add_band'),
]
