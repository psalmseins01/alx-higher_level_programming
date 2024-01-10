#!/usr/bin/python3
"""Module that defines a JSON file-reading function"""
import json


def load_from_json_file(filename):
    """Generates a Python object based on
       the contents of a specified JSON file.
    """
    with open(filename) as fhandle:
        return json.load(fhandle)
