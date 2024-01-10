#!/usr/bin/python3
"""Module defines append_write function"""


def append_write(filename="", text=""):
    """Appending a string to the end file
    """
    with open(filename, "a", encoding="utf-8") as fhandle:
        return fhandle.write(text)
