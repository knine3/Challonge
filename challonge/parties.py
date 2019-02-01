import requests as req
import json

# Basic Data
main_api = 'https://api.challonge.com/v1/'
api_key = "DeSvEj7MEldecZ7U5jvjPjRtyIttIy4HGdwlcPPR"
tournament_ID = 'sjq12ljh'

# Preparing API Request
url = main_api + 'tournaments/' + tournament_ID + '/participants'
payload = {'api_key': api_key}

# Requesting Data from API
response = req.get(url + '.json', params=payload)

# Obtaining JSON
participants = json.loads(response.text)

values2keep = ['id', 'name', 'seed', 'final_rank', 'group_player_ids']

def pprint(parsed):
    print(json.dumps(parsed, indent=2))

def parsing_json(participants):
    players = dict()

    for participant in participants:
        players [participant['participant']['name']] = {k:v for (k,v) in participant['participant'].items() if k in values2keep}

    return players

    

players = parsing_json(participants)
for player in players:
    print (f'{player} is ranked {players[player]["final_rank"]}')

