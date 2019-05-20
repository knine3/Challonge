import requests as req
from helper import pprint, parsing_json
import json

url = "https://api.challonge.com/v1/tournaments.json?state=ended"
key = "DeSvEj7MEldecZ7U5jvjPjRtyIttIy4HGdwlcPPR"

payload = {'api_key': key, 'state': 'ended'}

resp = req.get(url, params=payload)

print(resp.status_code)

tournaments = json.loads(resp.text)

# pprint(tournaments)

values2keep = ['id', 'name', 'completed_at', 'participants_count', 'game_name']

tournaments_d = parsing_json(tournaments, 'name', values2keep)


if __name__ == '__main__':
    for name in tournaments_d:
        if tournaments_d[name]['game_name'] is not None:
            if 'fifa' in tournaments_d[name]['game_name'].lower():
                print('\n#', name)
                for y in tournaments_d[name]:
                    print(y, ':', tournaments_d[name][y])
