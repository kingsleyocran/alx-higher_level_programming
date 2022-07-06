#!/usr/bin/python3
"""3-to_json_string.py
Function that returns the JSON representation of an object (string)
"""

import json


def to_json_string(my_obj):
    """Function returns the JSON representation of an object (string)
    - Returns: JSON representation
    """

    return json.dumps(my_obj)
