""" A collection of input methods that aren't necessarily buttons """

from rcfc.server import register_post_with_state, register_post_with_input
from rcfc.groups import convertGroup


class DIRECTIONAL:
    LEFT = "left"
    RIGHT = "right"


def slider(text, getter, input_range=(0, 100), group=None):
    min_value, max_value = input_range

    def wrapper(setter):
        slider = {
            "text": text,
            "type": "input.slider",
            "min": min_value,
            "max": max_value,
            "groups": convertGroup(group)
        }
        register_post_with_state(slider, getter, setter)
    return wrapper


def left_right_arrows(text, group=None):
    def wrapper(setter):
        arrows = {
            "text": text,
            "type": "input.leftright",
            "groups": convertGroup(group)
        }
        register_post_with_input(arrows, setter)
    return wrapper
