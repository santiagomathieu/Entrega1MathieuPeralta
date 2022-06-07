from django import forms
from peliculas.models import Peliculas,Series,Games

class Peliculas_form(forms.ModelForm):
    class Meta:
        model = Peliculas
        fields = '__all__'


class Series_form(forms.ModelForm):
    class Meta:
        model = Series
        fields = '__all__'


class Games_form(forms.ModelForm):
    class Meta:
        model = Games
        fields = '__all__'