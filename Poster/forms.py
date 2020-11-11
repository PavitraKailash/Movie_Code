from django import forms
from django.forms import ModelForm

from .models import Movies, Poster


class MovieForm(ModelForm):
    class Meta:
        model = Movies
        fields = '__all__'


class PosterForm(ModelForm):
    poster = forms.ImageField(required=True)

    class Meta:
        model = Poster
        fields = ['poster']
