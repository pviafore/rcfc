"""
A demo service for buttons
"""

from rcfc import button, server


@button.simple("easy")
def simple_button():
    """
    Print to console that it was easy
    """
    print("easy")


def main():
    """
    Main Method
    """
    server.start()

if __name__ == "__main__":
    main()
