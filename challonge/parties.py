import requests as req

main_api = 'https://api.challonge.com/v1/'
api_key = "DeSvEj7MEldecZ7U5jvjPjRtyIttIy4HGdwlcPPR"

tournament_ID = 'sjq12ljh'

url = main_api + 'tournaments/' + tournament_ID + '/participants.json'
payload = {'api_key': api_key}

party_data = req.get(url, params=payload)


def strip_dict(unDict):
    '''convert json to dict'''
    return unDict[next(iter(unDict))]


def getPartyID():
    players = {}
    for party in party_data.json():
        player = party['participant']
        players[player['name']] = player['id']

    return players


print(getPartyID())

getPartyID()
