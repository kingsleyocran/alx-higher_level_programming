#!/usr/bin/python3
"""4-from_json_string.py
Function that returns an object (Python data structure)
represented by a JSON string
"""

import json


def from_json_string(my_str):
    """Function returns a Python object from a json string
    - Returns: Python objects
    """

    return json.loads(my_str)
