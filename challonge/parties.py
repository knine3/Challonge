import requests as req
import json

main_api = 'https://api.challonge.com/v1/'
api_key = "DeSvEj7MEldecZ7U5jvjPjRtyIttIy4HGdwlcPPR"

tournament_ID = 'sjq12ljh'

url = main_api + 'tournaments/' + tournament_ID + '/participants'
payload = {'api_key': api_key}

party_data = req.get(url + '.json', params=payload)
party_json = json.loads(party_data.text)


def strip_dict(unDict):
    '''convert json to dict'''
    return unDict[next(iter(unDict))]


def getPlayers_ID():
    players = {}
    for party in party_json:
        player = party['participant']
        players[player['name']] = player['id']

    return players


def showPlayer(player_ID):
    '''returns a dictionary for certain particiapnt with party_ID'''
    player = req.get(url + '/' + str(player_ID) + '.json', params=payload)
    player_json = json.loads(player.text)
    return player_json['participant']


player_IDs = getPlayers_ID()

Fahad = showPlayer(player_IDs['Fahad'])
print(Fahad)

getPlayers_ID()
