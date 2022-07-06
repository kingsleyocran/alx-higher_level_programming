#!/usr/bin/python3
"""1-number_of_lines.py
Function that returns the number of lines of a text file
"""


def number_of_lines(filename=""):
    """ Function reads number of lines in a file
    - Args:
        filename (str): The name of the file to append to.
    - Returns:(int) counter.
    """
    if filename == "" or type(filename) != str:
        return 0
    counter = 0
    with open(filename, 'r') as f:
        for line in f:
            counter += 1
    return counter
