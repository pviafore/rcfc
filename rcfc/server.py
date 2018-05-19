"""
Runs the webserver for rcfc
"""
import inspect
import os

from bottle import run, route, get, hook, static_file, request, response

_buttons_registered = []


def getter_placeholder():
    """
    A placeholder that just returns None
    """
    return None


def _get_static_directory():
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), "static")


def clear_buttons():
    _buttons_registered.clear()


def register_post(button, setter):
    """
    Register a Post endpoint
    :param button: the info on the button
    :param setterc: the function to call when we post
    :return:
    """
    _validate_arguments(setter, 0)
    _register_button_action(button, getter_placeholder, setter)


def _register_button_action(button, getter, setter):
    next_index = len(_buttons_registered)

    def ignore_options_set():
        if(request.method == "OPTIONS"):
            return
        setter()

    route(f"/buttons/{next_index}", ["POST", "OPTIONS"], ignore_options_set)
    button["id"] = next_index
    button["getter"] = getter

    _buttons_registered.append(button)


def register_post_with_state(button, getter, setter):
    """
    Register a post endpoint that can change state
    :param button: the info on the button
    :param getter: the getter to call when the app asks for buttons
    :param setter: the setter that updates the state
    :return:
    """
    _validate_arguments(setter, 1)

    def set_value():
        setter(request.json['value'])

    _register_button_action(button, getter, set_value)


def _validate_arguments(func, expected):
    number_of_arguments = len(inspect.getargspec(func).args)
    if number_of_arguments != expected:
        raise InvalidArgumentsException(expected, number_of_arguments)


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
    buttons_with_state = [dict(b) for b in _buttons_registered]
    for button in buttons_with_state:
        button["state"] = button["getter"]()
        del button["getter"]
    return {"buttons": buttons_with_state}


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


class InvalidArgumentsException(ValueError):
    def __init__(self, expected, actual):
        message = f"Expected {expected} arguments, but got {actual} arguments"
        super().__init__(message)
