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
def simple_button():
    """
    Print to console that a button was pressed
    """
    print("You pressed a different button!")


@button.toggle("Toggle!")
def toggle_button(toggle):
    """ Toggle on or off """
    print(f"The toggle was set to {toggle}")


def main():
    """
    Main Method
    """
    server.start()


if __name__ == "__main__":
    main()
