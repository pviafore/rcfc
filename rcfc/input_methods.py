""" A collection of input methods that aren't necessarily buttons """

from rcfc.server import register_post_with_state
from rcfc.groups import convertGroup


def slider(text, getter, input_range=(0, 100), group=None):
    min_value, max_value = input_range

    def wrapper(setter):
        button = {
            "text": text,
            "type": "input.slider",
            "min": min_value,
            "max": max_value,
            "groups": convertGroup(group)
        }
        register_post_with_state(button, getter, setter)
    return wrapper
