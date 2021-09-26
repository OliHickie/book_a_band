from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_bands, name='all_bands'),
    path('<int:band_id>/', views.band_profile, name='band_profile'),
    path('add_band/', views.add_band, name='add_band'),
    path('add_review/<int:band_id>/', views.add_review, name='add_review'),
    path('edit_band/<int:band_id>/', views.edit_band, name='edit_band'),
]
