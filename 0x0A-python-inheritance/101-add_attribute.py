#!/usr/bin/python3
"""Module that defines a function that adds attributes to objects"""


def add_attribute(obj, attr, val):
    """Add new attr to an object
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, val)
