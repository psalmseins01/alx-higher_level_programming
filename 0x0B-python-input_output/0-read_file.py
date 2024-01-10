#!/usr/bin/python3
"""This module defines a text file-reading function"""


def read_file(filename=""):
    """Reads the contents of text file with UTF8"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
