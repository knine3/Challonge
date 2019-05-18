from json import dumps


def pprint(parsed):
    print(dumps(parsed, indent=2))


def parsing_json(json_response, key_name, values2keep):

    players = dict()

    '''
    participants is a list of multiple dicts
    Every dict consists of 1 key:value pair
    and we want to get the key name,
	so we are converting the dict -> list
	then accessing the list first element.
    '''

    parent = list(json_response[1])[0]

    for participant in json_response:
        players[participant[parent][key_name]] = {k: v for (k, v) in participant[parent].items() if k in values2keep}

    return players
