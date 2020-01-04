import pytest
import twitch_rivals.check_twitch as ct
from collections import namedtuple
import datetime


StreamInfo = namedtuple('StreamInfo', 'id game preview')
ChannelInfo = namedtuple('ChannelInfo', 'id name display_name game status logo video_banner profile_banner'
                                        ' profile_banner_background_color url description ')
GameInfo = namedtuple('GameInfo', 'name id box logo')


@pytest.mark.parametrize(
    "channels,expected",
    [
        (
            [{"url": "some-url"}],
            "some-url"
        ),
        (
            [{"url": "another-url"}],
            "another-url"
        ),
    ]
)
def test_get_first_channel_url(channels, expected):
    result = ct.get_first_channel_url(channels)
    assert result == expected


def test_get_first_channel_url_exception():
    broken_channels = [
        {"no-url": "some-url"}
    ]
    with pytest.raises(ct.CantFindUrlException):
        ct.get_first_channel_url(broken_channels)


@pytest.mark.parametrize(
    "expected",
    [
        (
            ChannelInfo(id='None', name='None', display_name='None',
                        game='None', status='None', description='None',
                        logo='None', video_banner='None', profile_banner='None',
                        profile_banner_background_color='None', url='None')
        )
    ]
)
def test_create_dummy_channel_info(expected):
    result = ct.create_dummy_channel_info()
    assert result == expected


@pytest.mark.parametrize(
    "expected",
    [
        (
            StreamInfo(id='None', game='None', preview='None')
        )
    ]
)
def test_create_dummy_stream_info(expected):
    result = ct.create_dummy_stream_info()
    assert result == expected


@pytest.mark.parametrize(
    "raw_channel, expected",
    [
        (
                {
                'mature': True,
                'status':
                'Player Picks chegaram! Sexta Monstra do Adolfera com Corridinhas no GTA, Começo da WL e muito mais!',
                'broadcaster_language': 'pt',
                'broadcaster_software': '',
                'display_name': 'adolfz',
                'game': 'FIFA 20',
                'language': 'en',
                'id': 26707340,
                'name': 'adolfz',
                'created_at': datetime.datetime(2011, 12, 10, 23, 30, 18, 952743),
                'updated_at': datetime.datetime(2020, 1, 4, 6, 54, 37, 36364),
                'partner': True,
                'logo': 'https://static-cdn.jtvnw.net/jtv_user_pictures/aca78bd5-e70b-4c14-8da8-68d60a74c8ba-profile_image-300x300.jpg',
                'video_banner': 'https://static-cdn.jtvnw.net/jtv_user_pictures/70fc1c8a-ec51-494f-94a4-014621778b73-channel_offline_image-1920x1080.png',
                'profile_banner': 'https://static-cdn.jtvnw.net/jtv_user_pictures/136fe6f4-06dd-468f-940c-0b7bf87da63a-profile_banner-480.jpeg',
                'profile_banner_background_color': '#000000',
                'url': 'https://www.twitch.tv/adolfz',
                'views': 4102776, 'followers': 179972,
                'broadcaster_type': '',
                'description': 'Depois de um ano e meio streamando na Mixer, estamos de volta a Twitch (e pra ficar). Acompanhem minhas livezinhas de FIFA e oq mais der vontade por aqui. ',
                'private_video': False,
                'privacy_options_enabled': False
                },
                ChannelInfo(
                    id=26707340, name='adolfz', display_name='adolfz',
                    game='FIFA 20',
                    status='Player Picks chegaram! Sexta Monstra do Adolfera com Corridinhas no GTA, Começo da WL e muito mais!',
                    description='Depois de um ano e meio streamando na Mixer, estamos de volta a Twitch (e pra ficar). Acompanhem minhas livezinhas de FIFA e oq mais der vontade por aqui. ',
                    logo='https://static-cdn.jtvnw.net/jtv_user_pictures/aca78bd5-e70b-4c14-8da8-68d60a74c8ba-profile_image-300x300.jpg',
                    video_banner='https://static-cdn.jtvnw.net/jtv_user_pictures/70fc1c8a-ec51-494f-94a4-014621778b73-channel_offline_image-1920x1080.png',
                    profile_banner='https://static-cdn.jtvnw.net/jtv_user_pictures/136fe6f4-06dd-468f-940c-0b7bf87da63a-profile_banner-480.jpeg',
                    profile_banner_background_color='#000000',
                    url='https://www.twitch.tv/adolfz'
                )
        )
    ]
)
def test_create_channel_info(raw_channel, expected):
    result = ct.create_channel_info(raw_channel)
    assert result == expected


@pytest.mark.parametrize(
    "raw_stream, expected",
    [
        (
            {
                'id': 36573168416,
                'game': 'FIFA 20',
                'broadcast_platform': 'live',
                'community_id': '',
                'community_ids': [],
                'viewers': 4649,
                'video_height': 1080,
                'average_fps': 60,
                'delay': 0,
                'created_at': datetime.datetime(2020, 1, 4, 1, 33, 44),
                'is_playlist': False,
                'stream_type': 'live',
                'preview': {
                    'small': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_adolfz-80x45.jpg',
                    'medium': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_adolfz-320x180.jpg',
                    'large': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_adolfz-640x360.jpg',
                    'template': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_adolfz-{width}x{height}.jpg'
                },
                'channel': {
                    'mature': True,
                    'status': 'Player Picks chegaram! Sexta Monstra do Adolfera com Corridinhas no GTA, Começo da WL e muito mais!',
                    'broadcaster_language': 'pt',
                    'broadcaster_software': '',
                    'display_name': 'adolfz',
                    'game': 'FIFA 20',
                    'language': 'en',
                    'id': 26707340,
                    'name': 'adolfz',
                    'created_at': datetime.datetime(2011, 12, 10, 23, 30, 18, 952743),
                    'updated_at': datetime.datetime(2020, 1, 4, 6, 54, 37, 36364),
                    'partner': True,
                    'logo': 'https://static-cdn.jtvnw.net/jtv_user_pictures/aca78bd5-e70b-4c14-8da8-68d60a74c8ba-profile_image-300x300.jpg',
                    'video_banner': 'https://static-cdn.jtvnw.net/jtv_user_pictures/70fc1c8a-ec51-494f-94a4-014621778b73-channel_offline_image-1920x1080.png',
                    'profile_banner': 'https://static-cdn.jtvnw.net/jtv_user_pictures/136fe6f4-06dd-468f-940c-0b7bf87da63a-profile_banner-480.jpeg',
                    'profile_banner_background_color': '#000000',
                    'url': 'https://www.twitch.tv/adolfz',
                    'views': 4102776,
                    'followers': 179984,
                    'broadcaster_type': '',
                    'description': 'Depois de um ano e meio streamando na Mixer, estamos de volta a Twitch (e pra ficar). Acompanhem minhas livezinhas de FIFA e oq mais der vontade por aqui. ',
                    'private_video': False,
                    'privacy_options_enabled': False
                }
            },
            StreamInfo(id=36573168416,
                       game='FIFA 20',
                       preview={
                           'small': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_adolfz-80x45.jpg',
                           'medium': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_adolfz-320x180.jpg',
                           'large': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_adolfz-640x360.jpg',
                           'template': 'https://static-cdn.jtvnw.net/previews-ttv/live_user_adolfz-{width}x{height}.jpg'
                       })
        )
    ]
)
def test_create_stream_info(raw_stream, expected):
    result = ct.create_stream_info(raw_stream)
    assert result == expected


@pytest.mark.parametrize(
    "raw_game, expected",
    [
        (
            {
                'game': {
                    'name': 'Escape From Tarkov',
                    'popularity': 193965,
                    'id': 491931,
                    'giantbomb_id': 53106,
                    'box': {
                        'large': 'https://static-cdn.jtvnw.net/ttv-boxart/Escape%20From%20Tarkov-272x380.jpg',
                        'medium': 'https://static-cdn.jtvnw.net/ttv-boxart/Escape%20From%20Tarkov-136x190.jpg',
                        'small': 'https://static-cdn.jtvnw.net/ttv-boxart/Escape%20From%20Tarkov-52x72.jpg',
                        'template':
                            'https://static-cdn.jtvnw.net/ttv-boxart/Escape%20From%20Tarkov-{width}x{height}.jpg'
                    },
                    'logo': {
                        'large': 'https://static-cdn.jtvnw.net/ttv-logoart/Escape%20From%20Tarkov-240x144.jpg',
                        'medium': 'https://static-cdn.jtvnw.net/ttv-logoart/Escape%20From%20Tarkov-120x72.jpg',
                        'small': 'https://static-cdn.jtvnw.net/ttv-logoart/Escape%20From%20Tarkov-60x36.jpg',
                        'template': 'https://static-cdn.jtvnw.net/ttv-logoart/Escape%20From%20Tarkov-{width}x{height}.jpg'
                    },
                    'localized_name': 'Escape From Tarkov',
                    'locale': 'en-us'
                },
                'viewers': 192156,
                'channels': 1293
            },
            GameInfo(
                name='Escape From Tarkov',
                id=491931,
                box={
                    'large': 'https://static-cdn.jtvnw.net/ttv-boxart/Escape%20From%20Tarkov-272x380.jpg',
                    'medium': 'https://static-cdn.jtvnw.net/ttv-boxart/Escape%20From%20Tarkov-136x190.jpg',
                    'small': 'https://static-cdn.jtvnw.net/ttv-boxart/Escape%20From%20Tarkov-52x72.jpg',
                    'template': 'https://static-cdn.jtvnw.net/ttv-boxart/Escape%20From%20Tarkov-{width}x{height}.jpg'
                },
                logo={
                    'large': 'https://static-cdn.jtvnw.net/ttv-logoart/Escape%20From%20Tarkov-240x144.jpg',
                    'medium': 'https://static-cdn.jtvnw.net/ttv-logoart/Escape%20From%20Tarkov-120x72.jpg',
                    'small': 'https://static-cdn.jtvnw.net/ttv-logoart/Escape%20From%20Tarkov-60x36.jpg',
                    'template': 'https://static-cdn.jtvnw.net/ttv-logoart/Escape%20From%20Tarkov-{width}x{height}.jpg'
                }
            )
        )
    ]
)
def test_create_game_info(raw_game, expected):
    result = ct.create_game_info(raw_game)
    assert result == expected

