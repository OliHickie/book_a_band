from django import forms
from .models import NewBooking


class BookingForm(forms.ModelForm):

    class Meta:
        model = NewBooking
        fields = ('client_name', 'email', 'contact_number',
                  'venue_name', 'venue_address1', 'venue_address2',
                  'county', 'postcode', 'wedding_date', 'start_time',
                  'emergency_contact', 'emergency_phone',
                  'additional_information')

    def __init__(self, *args, **kwargs):

        placeholders = {
            'client_name': 'Name',
            'email': 'Email Address',
            'contact_number': 'Phone Number',
            'venue_name': 'Name of Venue',
            'venue_address1': 'Street Address 1',
            'venue_address2': 'Street Address 2',
            'county': 'County',
            'postcode': 'Postcode',
            'wedding_date': 'Date',
            'start_time': 'Band Start Time',
            'emergency_contact': 'Emergency Contact Name',
            'emergency_phone': 'Emergency Contact Number',
            'additional_information': 'Additional Information',
        }

        super().__init__(*args, **kwargs)

        for field in self.fields:
            # Add Placeholder to each field
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # Add datepicker to wedding date field
            self.fields['wedding_date'].widget.attrs['id'] = 'datepicker'
            self.fields['start_time'].widget.attrs['class'] = 'timepicker'
            # Add class to each field
            self.fields[field].widget.attrs['class'] = 'booking-form-field'
            self.fields['start_time'].widget.attrs['class'] = 'booking-form-field'
            # remove form fields labels
            self.fields[field].label = False
