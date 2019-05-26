import requests as req
from api import key
from helper import pprint, json2dict
import json
from parties import parties

tournament_id = '6306852'
payload = {'api_key': key}
url = f'https://api.challonge.com/v1/tournaments/{tournament_id}/matches.json'

resp = req.get(url, params=payload)
matches = json.loads(resp.text)

# print(resp.status_code)
# pprint(matches)

values2keep = ['id', 'player1_id', 'player2_id', 'winner_id', 'loser_id', 'group_id', 'scores_csv']
matches_d = json2dict(matches, 'id', values2keep)

# List to store group IDs
grp = list()

# Determining Tournament Stages
for match in matches_d:
    iD = matches_d[match]['group_id']

    # Final Stage
    if iD is None:
        matches_d[match]['Stage'] = "Final"

    # Group Stages
    else:
        if iD not in grp:
            grp.append(iD)

        matches_d[match]['Stage'] = f'Group {grp.index(iD) + 1}'

    # Removing 'group_id' key.
    matches_d[match].pop('group_id')


for match in matches_d:
    print(matches_d[match])
