from django import forms
from .models import Band, BandReview


class BandForm(forms.ModelForm):

    class Meta:
        model = Band
        fields = '__all__'

    
class ReviewForm(forms.ModelForm):

    class Meta:
        model = BandReview
        fields = ('name', 'rating', 'review')
        exclude = ('band', 'date_added')
