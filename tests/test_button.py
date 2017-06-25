from rcfc import server, button


def do_nothing():
    pass


def test_simple_button_registration():

    button.simple("this is a button")(do_nothing)
    expected = {"text": "this is a button",
                "type": "button.simple",
                "id": 0}
    assert server.get_buttons_registered() == {"buttons": [expected]}
