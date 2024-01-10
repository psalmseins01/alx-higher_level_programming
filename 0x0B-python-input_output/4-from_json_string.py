#!/usr/bin/python3
""" Within this module, there is a function
    defined for converting JSON data into an object
"""


import json


def from_json_string(my_str):
    """ Provides the Python object
        representation corresponding to a JSON string
    """
    return json.loads(my_str)
