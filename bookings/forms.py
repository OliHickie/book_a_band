from django import forms
from .models import NewBooking


class BookingForm(forms.ModelForm):

    class Meta:
        model = NewBooking
        exclude = ('email', 'band_name', 'price')
        fields = ('client_name', 'contact_number',
                  'venue_name', 'venue_address1', 'venue_address2',
                  'county', 'postcode', 'wedding_date', 'start_time',
                  'emergency_contact', 'emergency_phone',
                  'additional_information')

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields:
            # Add date and time pickers
            self.fields['wedding_date'].widget.attrs['id'] = 'datepicker'
            self.fields['wedding_date'].widget.attrs['autocomplete'] = 'off'
            self.fields['start_time'].widget.attrs['id'] = 'timepicker'
            self.fields['start_time'].widget.attrs['autocomplete'] = 'off'
            self.fields['wedding_date'].widget.attrs['readonly'] = 'readonly'

            # Add class to each field
            self.fields[field].widget.attrs['class'] = 'booking-form-field'
            self.fields[field].widget.attrs['class'] = 'form-control'
