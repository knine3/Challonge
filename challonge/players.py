import requests as req
from json import loads
from player import Player
from api import key


tournament_ID = '6276700'


class Players():
    def __init__(self, tournament_ID, key):
        self._parsedJson = str()
        self._playersList = list()
        self.setParsedJson(tournament_ID, key)

    def setParsedJson(self, tournament_ID, key):
        url = 'https://api.challonge.com/v1/tournaments/' + tournament_ID + '/participants.json'
        payload = {'api_key': key}

        # Requesting Data from API
        response = req.get(url, params=payload)

        # Obtaining JSON
        self._parsedJson = loads(response.text)

    def getParsedJson(self):
        return self._parsedJson

    def setPlayersList(self):
        self._parsedJson

        for participant in self._parsedJson:
            # Accessing the main dict
            party = participant['participant']
            player = Player()
            player.setID(party['id'])
            player.setName(party['name'])
            player.setRank(party['final_rank'])
            player.setGroupID(party['group_player_ids'])

            self._playersList.append(player)

    def getPlayersList(self):
        return self._playersList

    def __str__(self):
        outp = str()
        for player in self._playersList:
            outp += (player.__str__() + '\n')

        return f'[\n{outp}]'


if __name__ == '__main__':
    players = Players(tournament_ID, key)
    players.setPlayersList()

    print(33 * "#")
    playerlist = players.getPlayersList()

    print(players)
