import requests
from get_pokemon import save_pokemon_info_and_image
def get_pokemon_by_type(pokemon_type):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon?limit=100')
    if response.status_code == 200:
        pokemon_data = response.json()
        pokemon_list = []
        for pokemon in pokemon_data['results']:
            pokemon_info = requests.get(pokemon['url']).json()
            types = [t['type']['name'].capitalize() for t in pokemon_info['types']]
            if pokemon_type.capitalize() in types:
                pokemon_list.append(pokemon['name'].capitalize())
                save_pokemon_info_and_image(pokemon['name'])
        return pokemon_list
    return None

pokemon_list = get_pokemon_by_type('Fire')
if pokemon_list:
    print(f'List of Pokemons with type "Fire": {pokemon_list}')
else:
    print('Failed to get Pokemon list')