from django.db import models


class NewBooking(models.Model):

    client_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    contact_number = models.CharField(max_length=14, null=False, blank=False)
    venue_name = models.CharField(max_length=50, null=False, blank=False)
    venue_address1 = models.CharField(max_length=80, null=False, blank=False)
    venue_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=False, blank=False)
    postcode = models.CharField(max_length=10, null=False, blank=False)
    wedding_date = models.DateField()
    start_time = models.CharField(max_length=10, null=False, blank=False)
    duration = models.IntegerField(null=False, blank=False)
    emergency_contact = models.CharField(
        max_length=50, null=False, blank=False)
    emergency_phone = models.CharField(
        max_length=14, null=False, blank=False)
    additional_information = models.TextField(null=True, blank=True)
    booking_created_at = models.DateTimeField(auto_now_add=True)
    booking_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client_name
