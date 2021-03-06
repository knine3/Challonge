import requests as req
from api import key
from helper import pprint, json2dict
import json
from parties import parties
import pandas
import csv

# tournament_ids = ['6323767']
data = pandas.read_csv('tournaments.csv')
tournament_ids = data.id.tolist()

for tournament_id in tournament_ids:
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

    players = parties(str(tournament_id), key)

    def id2name(iD, stage):

        for player in players:
            if stage == 'Final':
                if iD == players[player]['id']:
                    return player
                if players[player]['id'] is None:
                    return 'Draw'
            else:
                if iD == players[player]['group_player_ids'][0]:
                    return player
                if players[player]['id'] is None:
                    return 'Draw'

    for match in matches_d:
        winner_id = matches_d[match]['winner_id']
        player1_id = matches_d[match]['player1_id']
        player2_id = matches_d[match]['player2_id']
        stage = matches_d[match]['Stage']

        matches_d[match]['P1'] = id2name(player1_id, stage)
        matches_d[match]['P2'] = id2name(player2_id, stage)
        matches_d[match]['Winner'] = id2name(winner_id, stage)

        for e in ['player1_id', 'player2_id', 'winner_id', 'loser_id']:
            matches_d[match].pop(e)

    for match in matches_d:
        score = matches_d[match]['scores_csv']
        if score != '':
            score = score.split('-')
            matches_d[match]['P1_score'], matches_d[match]['P2_score'] = score[0], score[1]

        else:
            matches_d[match]['P1_score'], matches_d[match]['P2_score'] = 0, 0

        matches_d[match].pop('scores_csv')

    # for player in players:
    #     print(player)

    for match in matches_d:
        print(matches_d[match])

    if tournament_ids.index(tournament_id) == 0:
        with open('matches.csv', mode='w+') as csv_file:
            fieldnames = ['id', 'Stage', 'P1', 'P2', 'Winner', 'P1_score', 'P2_score']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for match in matches_d:
                writer.writerow(matches_d[match])
    else:
        with open('matches.csv', mode='a') as csv_file:
            fieldnames = ['id', 'Stage', 'P1', 'P2', 'Winner', 'P1_score', 'P2_score']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            for match in matches_d:
                writer.writerow(matches_d[match])
