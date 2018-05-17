from unittest.mock import patch

import pytest

from rcfc import server, button


def do_nothing():
    pass


@patch("bottle.Bottle.route")
def test_simple_button_registration(mock_route):
    server.clear_buttons()
    button.simple("this is a button")(do_nothing)
    expected = {"text": "this is a button",
                "type": "button.simple",
                "id": 0}
    assert server.get_buttons_registered() == {"buttons": [expected]}

    mock_route.assert_called_once_with("/buttons/0",
                                       ["POST", "OPTIONS"],
                                       do_nothing)


@patch("bottle.Bottle.route")
def test_button_registration_fails_when_arguments(mock_route):
    server.clear_buttons()
    with pytest.raises(server.InvalidArgumentsException):
        button.simple("this is a button")(do_nothing)
    assert server.get_buttons_registered() == {'buttons': []}
    mock_route.assert_not_called()


@patch("bottle.Bottle.route")
def test_slider_button_registration(mock_route):
    server.clear_buttons()
    button.toggle("Toggle Button")(do_nothing)
    expected = {"text": "Toggle Button",
                "type": "button.toggle",
                "id": 0}
    assert server.get_buttons_registered() == {"buttons": [expected]}

    mock_route.assert_called_once_with("/buttons/0",
                                       ["POST", "OPTIONS"],
                                       do_nothing)
