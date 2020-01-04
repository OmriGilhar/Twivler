import pytest
import twitch_rivals.twitchlib as tl
import datetime


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
    result = tl.get_first_channel_url(channels)
    assert result == expected


def test_get_first_channel_url_exception():
    broken_channels = [
        {"no-url": "some-url"}
    ]
    with pytest.raises(tl.CantFindUrlException):
        tl.get_first_channel_url(broken_channels)


@pytest.mark.parametrize(
    "expected",
    [
        (
            tl.ChannelInfo(
                id='None',
                name='None',
                display_name='None',
                game='None',
                status='None',
                description='None',
                logo='None',
                video_banner='None',
                profile_banner='None',
                profile_banner_background_color='None',
                url='None'
            )
        )
    ]
)
def test_create_dummy_channel_info(expected):
    result = tl.create_dummy_channel_info()
    assert result == expected


@pytest.mark.parametrize(
    "expected",
    [
        (
            tl.StreamInfo(id='None', game='None', preview='None')
        )
    ]
)
def test_create_dummy_stream_info(expected):
    result = tl.create_dummy_stream_info()
    assert result == expected


@pytest.mark.parametrize(
    "raw_channel, expected",
    [
        (
            {
                'mature': True,
                'status':
                    'blabla bla bla bla',
                    'broadcaster_language': 'pt',
                    'broadcaster_software': '',
                    'display_name': 'player-display-name',
                    'game': 'game-name',
                    'language': 'en',
                    'id': 12345678,
                    'name': 'player-display-name',
                    'created_at': datetime.datetime(2011, 1, 1, 1, 1, 1, 1),
                    'updated_at': datetime.datetime(2011, 1, 1, 1, 1, 1, 1),
                    'partner': True,
                    'logo': 'some-logo',
                    'video_banner': 'video-banner-url',
                    'profile_banner': 'profile-banner',
                    'profile_banner_background_color': '#000000',
                    'url': 'https://www.twitch.tv/player-display-name',
                    'views': 1234567, 'followers': 1234567,
                    'broadcaster_type': '',
                    'description': 'some description',
                    'private_video': False,
                    'privacy_options_enabled': False
            },
            tl.ChannelInfo(
                id=12345678, name='player-display-name',
                display_name='player-display-name',
                game='game-name',
                status='blabla bla bla bla',
                description='some description',
                logo='some-logo',
                video_banner='video-banner-url',
                profile_banner='profile-banner',
                profile_banner_background_color='#000000',
                url='https://www.twitch.tv/player-display-name'
            )
        )
    ]
)
def test_create_channel_info(raw_channel, expected):
    result = tl.create_channel_info(raw_channel)
    assert result == expected


@pytest.mark.parametrize(
    "raw_stream, expected",
    [
        (
            {
                'id': 36573168416,
                'game': 'game-name',
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
                    'small': 'small-logo-url',
                    'medium': 'medium-logo-url',
                    'large': 'large-logo-url',
                    'template': 'template-logo-url'
                },
                'channel': {
                    'mature': True,
                    'status': 'blabla bla bla bla',
                    'broadcaster_language': 'pt',
                    'broadcaster_software': '',
                    'display_name': 'player-display-name',
                    'game': 'game-name',
                    'language': 'en',
                    'id': 12345678,
                    'name': 'player-display-name',
                    'created_at': datetime.datetime(2011, 1, 1, 1, 1, 1, 1),
                    'updated_at': datetime.datetime(2011, 1, 1, 1, 1, 1, 1),
                    'partner': True,
                    'logo': 'some-logo-url',
                    'video_banner': 'video-banner-url',
                    'profile_banner': 'profile-banner',
                    'profile_banner_background_color': '#000000',
                    'url': 'https://www.twitch.tv/player-display-name',
                    'views': 1234567,
                    'followers': 179984,
                    'broadcaster_type': '',
                    'description': 'some description',
                    'private_video': False,
                    'privacy_options_enabled': False
                }
            },
            tl.StreamInfo(id=36573168416,
                          game='game-name',
                          preview={
                              'small': 'small-logo-url',
                              'medium': 'medium-logo-url',
                              'large': 'large-logo-url',
                              'template': 'template-logo-url'
                          })
        )
    ]
)
def test_create_stream_info(raw_stream, expected):
    result = tl.create_stream_info(raw_stream)
    assert result == expected


@pytest.mark.parametrize(
    "raw_game, expected",
    [
        (
            {
                'game': {
                    'name': 'game-name',
                    'popularity': 123456,
                    'id': 123456,
                    'giantbomb_id': 123456,
                    'box': {
                        'large': 'large-box',
                        'medium': 'medium-box',
                        'small': 'small-box',
                        'template': 'template-box'
                    },
                    'logo': {
                        'large': 'large-logo-url',
                        'medium': 'medium-logo-url',
                        'small': 'small-logo-url',
                        'template': 'template-logo-url'
                    },
                    'localized_name': 'game-name',
                    'locale': 'en-us'
                },
                'viewers': 192156,
                'channels': 1293
            },
            tl.GameInfo(
                name='game-name',
                id=123456,
                box={
                    'large': 'large-box',
                    'medium': 'medium-box',
                    'small': 'small-box',
                    'template': 'template-box'
                },
                logo={
                    'large': 'large-logo-url',
                    'medium': 'medium-logo-url',
                    'small': 'small-logo-url',
                    'template': 'template-logo-url'
                }
            )
        )
    ]
)
def test_create_game_info(raw_game, expected):
    result = tl.create_game_info(raw_game)
    assert result == expected
