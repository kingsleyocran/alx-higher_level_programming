#!/usr/bin/python3
"""5-save_to_json_file.py
Function that writes an Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Accepts Python object and sends JSON representation to file
    - Args:
            my_obj: any pyhton object
            filename (str): file name
    - Returns: none
    """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
