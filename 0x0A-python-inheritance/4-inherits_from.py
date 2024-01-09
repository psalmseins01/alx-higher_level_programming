#!/usr/bin/python3
"""If the object is an instance of a class that
inherited from the specified class
"""


def inherits_from(obj, a_class):
    """Returns 'True' if object is an instance of a class that inherited
    (directly or indirectly) from the specified class else returns 'False'
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
