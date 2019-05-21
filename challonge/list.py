import requests as req
from helper import pprint, json2dict
from parties import parties
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

# Retrieving winners and runners-up from all tournaments
for tournie in tournaments_d:
    t_ID = str(tournaments_d[tournie]['id'])
    players = parties(t_ID, key)

    for name in players:
        if players[name]['final_rank'] == 1:
            tournaments_d[tournie]['winner'] = name
        elif players[name]['final_rank'] == 2:
            tournaments_d[tournie]['runner-up'] = name


# Writing the tournaments data to csv
with open('tournaments.csv', mode='w+') as csv_file:
    fieldnames = ['id', 'name', 'completed_at', 'participants_count', 'game_name', 'winner', 'runner-up']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for tournie in tournaments_d:
        if 'fifa' in tournaments_d[tournie]['game_name'].lower():
            writer.writerow(tournaments_d[tournie])
