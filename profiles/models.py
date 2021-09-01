from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    A user profile model to store user details
    and display uaser's bookings
    """
    # each user can only have one profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    default_client_name = models.CharField(max_length=50, null=True, blank=True)
    default_email = models.EmailField(max_length=254, null=True, blank=True)
    default_contact_number = models.CharField(max_length=14, null=True, blank=True)
    default_venue_name = models.CharField(max_length=50, null=True, blank=True)
    default_venue_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_venue_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=10, null=True, blank=True)
    default_wedding_date = models.DateField()

    def __str__(self):
        return self.default_client_name
