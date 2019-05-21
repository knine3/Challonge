import requests as req
from helper import pprint, json2dict
import json
import csv

url = "https://api.challonge.com/v1/tournaments.json?state=ended"
key = "DeSvEj7MEldecZ7U5jvjPjRtyIttIy4HGdwlcPPR"

payload = {'api_key': key, 'state': 'ended'}

resp = req.get(url, params=payload)

print(resp.status_code)

tournaments = json.loads(resp.text)

values2keep = ['id', 'name', 'completed_at', 'participants_count', 'game_name']
tournaments_d = json2dict(tournaments, 'name', values2keep)

# Writing the tournaments data to csv
with open('tournaments.csv', mode='w+') as csv_file:
    fieldnames = ['id', 'name', 'completed_at', 'participants_count', 'game_name']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for tournie in tournaments_d:
        if 'fifa' in tournaments_d[tournie]['game_name'].lower():
            writer.writerow(tournaments_d[tournie])
