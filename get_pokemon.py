import os
import requests
from translate import translate

def get_pokemon_info(name):
    name = translate(name)
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
    if response.status_code == 200:
        pokemon_data = response.json()
        res = {}
        info = []
        info.append(f'Name: {pokemon_data["name"].capitalize()}')
        info.append(f'Height: {pokemon_data["height"] / 10} m')
        info.append(f'Weight: {pokemon_data["weight"] / 10} kg')
        types = ', '.join([t['type']['name'].capitalize() for t in pokemon_data['types']])
        info.append(f'Types: {types}')
        abilities = ', '.join([a['ability']['name'].capitalize() for a in pokemon_data['abilities']])
        info.append(f'Abilities: {abilities}')
        res["info"] = info
        res['url'] = pokemon_data['sprites']['front_default']
        res['url2'] = pokemon_data['sprites']['back_default']
        return res
    return None

def save_pokemon_info(name, folder):
    info = get_pokemon_info(name)
    if info:
        filename = os.path.join(folder, f'{name}.txt')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(info))
        return filename
    return None

def save_pokemon_image(name, folder):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
    if response.status_code == 200:
        pokemon_data = response.json()
        image_url = pokemon_data['sprites']['front_default']
        response = requests.get(image_url)
        if response.status_code == 200:
            filename = os.path.join(folder, f'{name}.png')
            with open(filename, 'wb') as f:
                f.write(response.content)
            return filename
    return None

def save_pokemon_info_and_image(name):
    folder = name.lower()
    os.makedirs(folder, exist_ok=True)
    info_filename = save_pokemon_info(name, folder)
    image_filename = save_pokemon_image(name, folder)
    return (info_filename, image_filename)
