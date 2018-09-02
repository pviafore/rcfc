"""
A collection of buttons to be displayed in the GUI
"""

from rcfc.server import register_post, register_post_with_state
from rcfc.groups import convertGroup


def simple(text, group=None):
    """ A simple press-button decorator that takes a title """
    def wrapper(func):
        register_post({"text": text,
                       "type": "button.simple",
                       "groups": convertGroup(group)},
                      func)
    return wrapper


def toggle(text, getter, group=None):
    """ A on/off slider toggle """
    def wrapper(setter):
        button = {"text": text,
                  "type": "button.toggle",
                  "groups": convertGroup(group)}
        register_post_with_state(button, getter, setter)
    return wrapper
