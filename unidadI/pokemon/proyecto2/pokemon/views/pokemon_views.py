import requests
from django.shortcuts import render

def buscar_pokemon(request):
    pokemon_name = request.GET.get('name', '')
    pokemon_data = {}
    
    if pokemon_name:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
        if response.status_code == 200:
            pokemon_data = response.json()
            print(pokemon_data)  # Esto imprimirá la respuesta completa de la API en la consola.
    
    return render(request, 'pokemon/buscar_pokemon.html', {'pokemon': pokemon_data})
