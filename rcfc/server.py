"""
Runs the webserver for rcfc
"""

from bottle import run, route, get, static_file

_buttons_registered = []


def register_post(button):
    """
    Register a Post endpoint
    :param text: the id of the button
    :param button_func: the function to call when we post
    :return:
    """
    next_index = len(_buttons_registered)
    route(f"/{next_index}", "POST", button["func"])
    _buttons_registered.append(button)


@get("/buttons")
def get_buttons_registered():
    """
    Get buttons registered
    :return: a dictionary containing buttons registered
    """
    return {"buttons": _buttons_registered}


@get("/")
def route_index():
    return static_file("index.html", root="rcfc/static")


@get("/index.js")
def route_js():
    return static_file("index.js", root="rcfc/static")


def start():
    """
    Starts our webserver on port 7232
    """
    run(host="0.0.0.0", port=7232)
