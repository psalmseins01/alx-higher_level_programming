#!/usr/bin/python3
"""Module defines a wrte_file function."""


def write_file(filename="", text=""):
    """Writing a str to a UTF8 text file"""
    with open(filename, "w", encoding="utf-8") as fhandle:
        return fhandle.write(text)
