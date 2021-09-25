from django.db import models

from bands.models import Band


class NewBooking(models.Model):
    band = models.ForeignKey(Band, null=False, blank=False, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    contact_number = models.CharField(max_length=14, null=False, blank=False)
    venue_name = models.CharField(max_length=50, null=False, blank=False)
    venue_address1 = models.CharField(max_length=80, null=False, blank=False)
    venue_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=False, blank=False)
    postcode = models.CharField(max_length=10, null=False, blank=False)
    wedding_date = models.DateField(null=False, blank=False)
    start_time = models.CharField(max_length=10, null=False, blank=False)
    emergency_contact = models.CharField(
        max_length=50, null=False, blank=False)
    emergency_phone = models.CharField(
        max_length=14, null=False, blank=False)
    additional_information = models.TextField(null=True, blank=True)
    booking_created_at = models.DateTimeField(auto_now_add=True)
    booking_updated_at = models.DateTimeField(auto_now=True)
    price = models.IntegerField(null=False, blank=False)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.client_name
