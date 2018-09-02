"""
A demo service for buttons
"""

from rcfc import button, server, input_methods


@button.simple("Easy")
def simple_button():
    """
    Print to console that it was easy
    """
    print("That was easy, wasn't it")


@button.simple("Button!")
def simple_button2():
    """
    Print to console that a button was pressed
    """
    print("You pressed a different button!")


@button.simple("Group Button!", group="Group A")
def simple_group_button():
    """
    Print to console that a button was pressed
    """
    print("You pressed a group button!")


@button.simple("Multiple Group Button!", group=["Group A", "Group B"])
def simple_group_button():
    """
    Print to console that a button was pressed
    """
    print("You pressed a multiple group button!")


bool_value = False
group_a_bool_value = False


def getter():
    """ Return our boolean value"""
    return bool_value


def getter_a():
    return group_a_bool_value


@button.toggle("Toggle!", getter)
def toggle_button(toggle):
    """ Toggle on or off """
    print(f"The toggle was set to {toggle}")
    global bool_value
    bool_value = toggle


@button.toggle("Toggle!", getter_a, group="Group A")
def toggle_group_button(toggle):
    """ Toggle on or off """
    print(f"The group toggle was set to {toggle}")
    global group_a_bool_value
    group_a_bool_value = toggle


slider_value = 20


@input_methods.slider("Slider", lambda: slider_value)
def simple_slider(val):
    global slider_value
    print(f"Value set to: {val}")
    slider_value = val


slider_value2 = 20


@input_methods.slider("Restricted Slider", lambda: slider_value2, (10, 30))
def simple_slider2(val):
    global slider_value2
    print(f"Value set to: {val}")
    slider_value2 = val


@input_methods.left_right_arrows("Arrows")
def arrows(val):
    print(f"Arrows were set to {val}")


rgb = (10, 20, 30)


def get_rgb():
    return rgb


@input_methods.colorpicker("Color picker", lambda: rgb)
def colorpicker(val):
    global rgb
    print(f"Color was picked: {val}")
    rgb = val


def main():
    """
    Main Method
    """
    server.start()


if __name__ == "__main__":
    main()
