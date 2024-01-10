#!/usr/bin/python3
"""Within this module, there is a function
   defined for writing data to a JSON file.
"""
import json


def save_to_json_file(my_obj, filename):
    """Saves an object to a text file in JSON format"""
    with open(filename, "w") as fh:
        json.dump(my_obj, fh)
