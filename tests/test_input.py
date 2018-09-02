from unittest.mock import patch

from rcfc import server, input_methods
from test_helpers import IgnoredArgument

input_value = 0


def set_input_value(val):
    global input_value
    input_value = val


@patch("bottle.Bottle.route")
def test_slider(mock_route):
    server.clear_buttons()
    input_methods.slider("Slider text", lambda: input_value)(set_input_value)
    expected = {"text": "Slider text",
                "type": "input.slider",
                "groups": [],
                "state": 0,
                "min": 0,
                "max": 100,
                "id": 0}
    assert server.get_buttons_registered() == {"buttons": [expected]}

    mock_route.assert_called_once_with("/buttons/0",
                                       ["POST", "OPTIONS"],
                                       IgnoredArgument())


@patch("bottle.Bottle.route")
def test_slider_with_range(mock_route):
    server.clear_buttons()
    input_methods.slider("Slider text",
                         lambda: input_value,
                         (10, 20))(set_input_value)
    expected = {"text": "Slider text",
                "type": "input.slider",
                "groups": [],
                "state": 0,
                "min": 10,
                "max": 20,
                "id": 0}
    assert server.get_buttons_registered() == {"buttons": [expected]}

    mock_route.assert_called_once_with("/buttons/0",
                                       ["POST", "OPTIONS"],
                                       IgnoredArgument())
