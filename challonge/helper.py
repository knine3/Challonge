from json import dumps


def pprint(parsed):
    print(dumps(parsed, indent=2))


def parsing_json(participants, parent, key, values2keep):
    players = dict()

    for participant in participants:
        players[participant[parent][key]] = {k: v for (k, v) in participant[parent].items() if k in values2keep}

    return players
