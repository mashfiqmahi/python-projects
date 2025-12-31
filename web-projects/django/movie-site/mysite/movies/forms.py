from django import forms
from .models import Movie

class RateMovieForm(forms.ModelForm):
    rating = forms.FloatField(
        label='Your Rating Out of 10 e.g. 7.5',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'max': 10, 'min': 0})
    )
    review = forms.CharField(
        label='Your Review',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Movie
        fields = ['rating', 'review']

class AddMovieForm(forms.Form):
    title = forms.CharField(
        label='Movie Title',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )