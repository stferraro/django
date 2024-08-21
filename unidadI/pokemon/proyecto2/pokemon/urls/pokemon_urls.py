from django.urls import path
from ..views.pokemon_views import buscar_pokemon

urlpatterns = [
    path('', buscar_pokemon, name='buscar_pokemon'),
]
