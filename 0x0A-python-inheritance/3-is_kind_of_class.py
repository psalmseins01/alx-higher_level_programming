#!/usr/bin/python3
"""Checks if object is an instance of a class
or inherited class
"""


def is_kind_of_class(obj, a_class):
    """Returns 'True' if object is an instance of a class
    or if the object is an instance of a class that inherited from
    the specified class ; otherwise 'False'
    """
    return (isinstance(obj, a_class))
