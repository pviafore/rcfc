"""
A demo service for buttons
"""

from rcfc import button, server


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


bool_value = False


def getter():
    """ Return our boolean value"""
    return bool_value


@button.toggle("Toggle!", getter)
def toggle_button(toggle):
    """ Toggle on or off """
    print(f"The toggle was set to {toggle}")
    global bool_value
    bool_value = toggle


def main():
    """
    Main Method
    """
    server.start()


if __name__ == "__main__":
    main()
