#!/usr/bin/python3
"""Module add_integer"""


def add_integer(a, b=98):
    """Add integer function
    Float arguments are typecasted to ints before addition is performed.
    Returns:
        addition of a and b (int)
    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return (int(a) + int(b))
