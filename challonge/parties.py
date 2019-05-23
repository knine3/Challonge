import requests as req
import json
from helper import pprint, json2dict
from api import key

tournament_ID = '6276700'


def parties(tournament_ID, key):
    # Preparing API Request
    url = 'https://api.challonge.com/v1/tournaments/' + tournament_ID + '/participants.json'
    payload = {'api_key': key}

    # Requesting Data from API
    response = req.get(url, params=payload)

    # Obtaining JSON
    participants = json.loads(response.text)
    values2keep = ['id', 'name', 'seed', 'final_rank', 'group_player_ids']

    players = json2dict(participants, 'name', values2keep)

    return players


if __name__ == '__main__':
    players = parties(tournament_ID, key)
    for player in players:
        print(f'{player} is ranked {players[player]["final_rank"]}')
