#!/usr/bin/python3
"""defines a Locked class"""


class LockedClass:
    """
    Do not instantiate any attribute unless is called first_name
    """

    __slots__ = ["first_name"]
