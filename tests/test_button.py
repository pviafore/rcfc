from unittest.mock import patch

import pytest

from rcfc import server, button
from test_helpers import IgnoredArgument


bool_value = False


def do_nothing():
    return bool_value


def set_bool(token_argument):
    global bool_value
    bool_value = token_argument


@patch("bottle.Bottle.route")
def test_simple_button_registration(mock_route):
    server.clear_buttons()
    button.simple("this is a button")(do_nothing)
    expected = {"text": "this is a button",
                "type": "button.simple",
                "groups": [],
                "state": None,
                "id": 0}
    assert server.get_buttons_registered() == {"buttons": [expected]}

    mock_route.assert_called_once_with("/buttons/0",
                                       ["POST", "OPTIONS"],
                                       IgnoredArgument())


@patch("bottle.Bottle.route")
def test_simple_button_registration_fails_when_arguments(mock_route):
    server.clear_buttons()
    with pytest.raises(server.InvalidArgumentsException):
        button.simple("this is a button")(set_bool)
    assert server.get_buttons_registered() == {'buttons': []}
    mock_route.assert_not_called()


@patch("bottle.Bottle.route")
def test_group_simple_button_registration(mock_route):
    server.clear_buttons()
    button.simple("Group Button", "Group A")(do_nothing)
    groups = server.get_buttons_registered()["buttons"][0]["groups"]
    assert groups == ["Group A"]


@patch("bottle.Bottle.route")
def test_multigroup_simple_button_registration(mock_route):
    server.clear_buttons()
    button.simple("Group Button", ["Group A", "Group B"])(do_nothing)
    groups = server.get_buttons_registered()["buttons"][0]["groups"]
    assert groups == ["Group A", "Group B"]


def mock_call(uri, headers, func):
    assert uri == "buttons/0"
    assert headers == ["POST", "OPTIONS"]


@patch("bottle.Bottle.route")
def test_toggle_button_registration(mock_route):
    server.clear_buttons()
    button.toggle("Toggle Button", do_nothing)(set_bool)
    expected = {"text": "Toggle Button",
                "type": "button.toggle",
                "groups": [],
                "state": False,
                "id": 0}

    mock_route.side_effect = mock_call
    assert server.get_buttons_registered() == {"buttons": [expected]}

    global bool_value
    bool_value = True
    expected["state"] = True
    assert server.get_buttons_registered() == {"buttons": [expected]}

    mock_route.assert_called_once_with("/buttons/0",
                                       ["POST", "OPTIONS"],
                                       IgnoredArgument())


@patch("bottle.Bottle.route")
def test_toggle_button_registration_with_invalid_args(mock_route):
    server.clear_buttons()
    with pytest.raises(server.InvalidArgumentsException):
        button.toggle("Toggle Button", do_nothing)(do_nothing)
    assert server.get_buttons_registered() == {'buttons': []}
    mock_route.assert_not_called()


@patch("bottle.Bottle.route")
def test_toggle_button_registration(mock_route):
    server.clear_buttons()
    button.toggle("Toggle Button", do_nothing, "Group A")(set_bool)
    groups = server.get_buttons_registered()["buttons"][0]["groups"]
    assert groups == ["Group A"]
