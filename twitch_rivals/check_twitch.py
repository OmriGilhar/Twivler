import twitch
import os
import json
from collections import namedtuple


StreamInfo = namedtuple('StreamInfo', 'id game preview')
ChannelInfo = namedtuple('ChannelInfo', 'id name display_name game status logo video_banner profile_banner'
                                        ' profile_banner_background_color url description ')
GameInfo = namedtuple('GameInfo', 'name id box logo')


class CantFindUrlException(Exception):
    pass


def pull_live_streams_by_game(client, game_name, limit=10):
    return client.streams.get_live_streams(game=game_name, limit=limit)


def get_first_channel_url(channels):
    try:
        return channels[0]["url"]
    except KeyError:
        raise CantFindUrlException("something went wrong")


def get_top_games(client, limit=10, offset=0):
    return client.games.get_top(limit=limit, offset=offset)


def create_game_info(game):
    return GameInfo(name=game['game']['name'], id=game['game']['id'], box=game['game']['box'],
                    logo=game['game']['logo'])


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


def create_stream_info(stream):
    return StreamInfo(id=stream['id'], game=stream['game'], preview=stream['preview'])


def create_channel_info(channel):
    return ChannelInfo(id=channel['id'], name=channel['name'], display_name=channel['display_name'],
                       game=channel['game'], status=channel['status'], description=channel['description'],
                       logo=channel['logo'], video_banner=channel['video_banner'],
                       profile_banner=channel['profile_banner'],
                       profile_banner_background_color=channel['profile_banner_background_color'], url=channel['url'])


def create_dummy_channel_info():
    return ChannelInfo(id='None', name='None', display_name='None', game='None', status='None', description='None',
                       logo='None', video_banner='None', profile_banner='None', profile_banner_background_color='None',
                       url='None')


def create_dummy_stream_info():
    return StreamInfo(id='None', game='None', preview='None')


def create_client(client_id, client_secret):
    # Create a client base on the client ID from the json file.
    client = twitch.TwitchClient(client_id=client_id)
    return client


if __name__ == '__main__':
    x = create_dummy_channel_info()
    print(type(x))