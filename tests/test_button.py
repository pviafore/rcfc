from unittest.mock import patch

import pytest

from rcfc import server, button

bool_value = False


def do_nothing():
    return bool_value


def do_nothing_arg(token_argument):
    pass


@patch("bottle.Bottle.route")
def test_simple_button_registration(mock_route):
    server.clear_buttons()
    button.simple("this is a button")(do_nothing)
    expected = {"text": "this is a button",
                "type": "button.simple",
                "state": None,
                "id": 0}
    assert server.get_buttons_registered() == {"buttons": [expected]}

    mock_route.assert_called_once_with("/buttons/0",
                                       ["POST", "OPTIONS"],
                                       do_nothing)


@patch("bottle.Bottle.route")
def test_simple_button_registration_fails_when_arguments(mock_route):
    server.clear_buttons()
    with pytest.raises(server.InvalidArgumentsException):
        button.simple("this is a button")(do_nothing_arg)
    assert server.get_buttons_registered() == {'buttons': []}
    mock_route.assert_not_called()


@patch("bottle.Bottle.route")
def test_toggle_button_registration(mock_route):
    server.clear_buttons()
    button.toggle("Toggle Button", do_nothing)(do_nothing_arg)
    expected = {"text": "Toggle Button",
                "type": "button.toggle",
                "state": False,
                "id": 0}
    assert server.get_buttons_registered() == {"buttons": [expected]}

    global bool_value
    bool_value = True
    expected["state"] = True
    assert server.get_buttons_registered() == {"buttons": [expected]}

    mock_route.assert_called_once_with("/buttons/0",
                                       ["POST", "OPTIONS"],
                                       do_nothing_arg)


@patch("bottle.Bottle.route")
def test_toggle_button_registration_with_invalid_args(mock_route):
    server.clear_buttons()
    with pytest.raises(server.InvalidArgumentsException):
        button.toggle("Toggle Button", do_nothing)(do_nothing)
    assert server.get_buttons_registered() == {'buttons': []}
    mock_route.assert_not_called()
