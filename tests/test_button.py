from unittest.mock import patch

from rcfc import server, button


def do_nothing():
    pass


@patch("bottle.Bottle.route")
def test_simple_button_registration(mock_route):
    button.simple("this is a button")(do_nothing)
    expected = {"text": "this is a button",
                "type": "button.simple",
                "id": 0}
    assert server.get_buttons_registered() == {"buttons": [expected]}

    mock_route.assert_called_once_with("/buttons/0", ["POST","OPTIONS"], do_nothing)
