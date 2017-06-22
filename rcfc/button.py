"""
A collection of buttons to be displayed in the GUI
"""

from rcfc.server import register_post


def simple(text):
    """ A simple press-button decorator that takes a title """
    def wrapper(func):
        register_post(text, func)
    return wrapper
