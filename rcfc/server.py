"""
Runs the webserver for rcfc
"""

from bottle import run, route, get, static_file, response

_buttons_registered = []


def register_post(button, func):
    """
    Register a Post endpoint
    :param button: the info on the button
    :param func: the function to call when we post
    :return:
    """
    next_index = len(_buttons_registered)
    route(f"/buttons/{next_index}", "POST", func)
    button["id"] = next_index
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
    """ Route to the index page """
    return static_file("index.html", root="rcfc/static")


@get("/static/<path:path>")
def route_js(path):
    """ Route to the JS page"""
    if path not in ["index.js", "static.css"]:
        response.status = 404
        return
    return static_file(path, root="rcfc/static")


def start():
    """
    Starts our webserver on port 7232
    """
    print("You can view your buttons in a web-browser "\
          "by navigating to http://localhost:7232/")
    run(host="0.0.0.0", port=7232)
