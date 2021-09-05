from django import forms
from .models import UserProfile


class UserDetails(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('default_client_name', 'default_email',
                  'default_contact_number', 'default_venue_name',
                  'default_venue_address1', 'default_venue_address2',
                  'default_county', 'default_postcode', 'default_wedding_date')

    def __init__(self, *args, **kwargs):

        placeholders = {
            'default_client_name': 'Name',
            'default_email': 'Email Address',
            'default_contact_number': 'Phone Number',
            'default_venue_name': 'Name of Venue',
            'default_venue_address1': 'Street Address 1',
            'default_venue_address2': 'Street Address 2',
            'default_county': 'County',
            'default_postcode': 'Postcode',
            'default_wedding_date': 'Date of Wedding',
        }

        super().__init__(*args, **kwargs)

        for field in self.fields:
            # Add Placeholder to each field
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # Add class to each field
            self.fields[field].widget.attrs['class'] = 'user-details-form-field'
            # remove form fields labels
            self.fields[field].label = False
