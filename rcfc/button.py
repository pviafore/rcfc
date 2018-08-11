"""
A collection of buttons to be displayed in the GUI
"""

from rcfc.server import register_post, register_post_with_state


def simple(text, group=None):
    """ A simple press-button decorator that takes a title """
    def wrapper(func):
        register_post({"text": text,
                       "type": "button.simple",
                       "groups": _convertGroup(group)},
                      func)
    return wrapper


def toggle(text, getter, group=None):
    """ A on/off slider toggle """
    def wrapper(setter):
        button = {"text": text, "type": "button.toggle", "groups": _convertGroup(group)}
        register_post_with_state(button, getter, setter)
    return wrapper

def _convertGroup(group):
    if(isinstance(group, str)):
        return [group]
    if group is None:
        return []
    assert isinstance(group, list), f"The group: {group} must be a list or string"
    return group