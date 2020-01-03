import twitch
import os
import json


class CantFindUrlException(Exception):
    pass


def pull_live_streams_by_game(client, game_name, limit=10):
    return client.streams.get_live_streams(game=game_name, limit=limit)


def get_first_channel_url(channels):
    try:
        return channels[0]["url"]
    except KeyError:
        raise CantFindUrlException("something went wrong")


def get_twitch_channels(client, name):
    return client.search.channels(name)


def pars_twitch_info(json_path):
    with open(json_path) as upload:
        json_data = json.load(upload)
    client_id = json_data['twitch-client-id']
    client_secret = json_data['twitch-client-secret']
    return client_id, client_secret


def get_client_id():
    ##############################################
    # WIP - Temp lines (until we design a better way)
    # build the path to twitch info json then pars the json and return the client ID and the client Secret
    dir_path = os.path.dirname(os.path.realpath(__file__))
    twitch_json_path = os.path.abspath(os.path.join(dir_path, '..'))
    twitch_json_path = os.path.abspath(os.path.join(twitch_json_path, '..'))
    twitch_json_path = os.path.abspath(
        os.path.join(twitch_json_path, 'twitch_info.json'))
    client_id, client_secret = pars_twitch_info(twitch_json_path)
    ##############################################
    return client_id, client_secret


def create_client(client_id, client_secret):
    # Create a client base on the client ID from the json file.
    client = twitch.TwitchClient(client_id=client_id)
    return client
