import requests as req
import json
from helper import pprint, parsing_json

# Basic Data
main_api = 'https://api.challonge.com/v1/'
api_key = "DeSvEj7MEldecZ7U5jvjPjRtyIttIy4HGdwlcPPR"
tournament_ID = '6276700'

# Preparing API Request
url = main_api + 'tournaments/' + tournament_ID + '/participants'
payload = {'api_key': api_key}

# Requesting Data from API
response = req.get(url + '.json', params=payload)

# Obtaining JSON
participants = json.loads(response.text)

values2keep = ['id', 'name', 'seed', 'final_rank', 'group_player_ids']


players = parsing_json(participants, 'name', values2keep)

if __name__ == '__main__':
    for player in players:
        print(f'{player} is ranked {players[player]["final_rank"]}')
