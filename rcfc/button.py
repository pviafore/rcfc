"""
A collection of buttons to be displayed in the GUI
"""

from rcfc.server import register_post, register_post_with_state


def simple(text):
    """ A simple press-button decorator that takes a title """
    def wrapper(func):
        register_post({"text": text,  "type": "button.simple"}, func)
    return wrapper


def toggle(text, getter):
    """ A on/off slider toggle """
    def wrapper(setter):
        button = {"text": text, "type": "button.toggle"}
        register_post_with_state(button, getter, setter)
    return wrapper
