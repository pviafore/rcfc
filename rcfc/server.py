"""
Runs the webserver for rcfc
"""

from bottle import run, route, get
from json import dumps

_buttons_registered = []


def register_post(text, button_func):
    """
    Register a Post endpoint
    :param text: the id of the button
    :param button_func: the function to call when we post
    :return:
    """
    route("/"+text, "POST", button_func)
    _buttons_registered.append({"id": text})


@get("/buttons")
def get_buttons_registered():
    """
    Get buttons registered
    :return: a dictionary containing buttons registered
    """
    return {"buttons": _buttons_registered}


def start():
    """
    Starts our webserver on port 7232
    """
    run(host="0.0.0.0", port=7232)
