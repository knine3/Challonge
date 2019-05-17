import requests as r
import json
from helper import pprint

# Pre-reqs
key = 'DeSvEj7MEldecZ7U5jvjPjRtyIttIy4HGdwlcPPR'
api = 'https://api.challonge.com/v1'
tournament_id = '6286532'

# Main URL
url = 'https://api.challonge.com/v1/tournaments/' + tournament_id + '/matches.json'
payload = {'api_key': key}

# Making request
response = r.get(url, params=payload)

# Check
# print(response.status_code)

matches = json.loads(response.text)

pprint(matches)
