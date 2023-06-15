import json

import requests


url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api'
response = requests.get(f'{url}/all.json')
info = {}
for one_dict in response.json():
    if one_dict['name'] == 'Hulk' or one_dict['name'] == 'Captain America' or one_dict['name'] == 'Thanos':
        info[one_dict['name']] = one_dict['powerstats']['intelligence']
for hero, each_intelligence in info.items():
    if each_intelligence == max(info.values()):
        print(f'Самый умный супергерой - {hero}')

