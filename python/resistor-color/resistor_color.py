"""Resistor colors"""


def color_code(color):
    """Return resistor digit value for color"""
    return colors().index(color)


def colors():
    """Return list of resistor colors"""
    return [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
    ]
