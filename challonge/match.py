import requests as req
from api import key
from helper import pprint, json2dict
import json
from parties import parties

tournament_id = '6311987'
payload = {'api_key': key}
url = f'https://api.challonge.com/v1/tournaments/{tournament_id}/matches.json'

resp = req.get(url, params=payload)
matches = json.loads(resp.text)

# print(resp.status_code)
# pprint(matches)

values2keep = ['id', 'player1_id', 'player2_id', 'winner_id', 'loser_id', 'group_id', 'scores_csv']
matches_d = json2dict(matches, 'id', values2keep)

for match in matches_d:
    print(match, matches_d[match])
