#!/usr/bin/python3
"""1-write_file.py
Function that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """ Function writes text into file
    Returns: none
    """
    with open(filename, 'w') as f:
        return f.write(text)
