"""
Runs the webserver for rcfc
"""
import os

from bottle import run, route, get, hook, static_file, response

_buttons_registered = []


def _get_static_directory():
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), "static")


def clear_buttons():
    _buttons_registered.clear()


def register_post(button, func):
    """
    Register a Post endpoint
    :param button: the info on the button
    :param func: the function to call when we post
    :return:
    """
    next_index = len(_buttons_registered)
    route(f"/buttons/{next_index}", ["POST", "OPTIONS"], func)
    button["id"] = next_index
    _buttons_registered.append(button)


@hook('after_request')
def enable_cors():
    """
    You need to add some headers to each request.
    Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
    """

    response.headers['Access-Control-Allow-Origin'] = '*'

    methods = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Methods'] = methods

    headers = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
    response.headers['Access-Control-Allow-Headers'] = headers


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
    return route_static("index.html")


@get("/static/<path:path>")
def route_static(path):
    """ Route to the JS page"""
    if path not in ["index.js", "static.css", "index.html"]:
        response.status = 404
        return
    return static_file(path, root=_get_static_directory())


def start():
    """
    Starts our webserver on port 7232
    """
    print("You can view your buttons in a web-browser "
          "by navigating to http://localhost:7232/")
    run(host="0.0.0.0", port=7232)
