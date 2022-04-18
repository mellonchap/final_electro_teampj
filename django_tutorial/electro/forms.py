from dataclasses import field
from django.forms import ModelForm
from .models import Place

class PlaceForm(ModelForm):
    class Meta:
        model = Place
        # field = ['country','population']
        fields = '__all__'