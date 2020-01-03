import pytest
import twitch_rivals.check_twitch as ct


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
