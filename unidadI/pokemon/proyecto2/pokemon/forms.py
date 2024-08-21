from django import forms

class PokemonForm(forms.Form):
    nombre = forms.CharField(label='Nombre del Pokémon', max_length=100)
