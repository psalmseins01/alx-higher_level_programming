#!/usr/bin/python3
"""If the object is an instance of a class"""


def is_same_class(obj, a_class):
    """Returns true if object is exactly an instance of the
    class else return false
    """
    return (type(obj) == a_class)
