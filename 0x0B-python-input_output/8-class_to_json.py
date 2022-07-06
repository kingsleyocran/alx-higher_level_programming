#!/usr/bin/python3
"""8-class_to_json.py
Function that returns the dictionary description with simple data structure
"""


def class_to_json(obj):
    """Accepts obj and returns the dictionary description with simple
    data structure
    - Returns: dictionary description of obj
    """
    return obj.__dict__
