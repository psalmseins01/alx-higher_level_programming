#!/usr/bin/python3
"""

Module composed of a function that adds two numbers

"""


def add_integer(a, b=98):
    """ Function that adds two integers or  two floating point numbers

    Args:
        a: argument a
        b: argument b

    Returns:
        The result of addition of the two given numbers

    Raises:
        TypeError: If a or b are not integers or floats numbers

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
