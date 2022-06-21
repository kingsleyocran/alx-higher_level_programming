#!/usr/bin/python3
"""Magic class from a given ByteCode."""


import math


class MagicClass:
    """Initialization of the MagicClass."""
    def __init__(self, radius=0):
        """Initializes method
        Args:
            radius (int): radius value of the circle class
        Returns:
            None
        """
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """Calculation of the circumference.
        Returns:
            int: circumference of the circle
        """
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """Calculation of the circumference.
        Returns:
            int: circumference of the circle
        """
        return 2 * math.pi * self._MagicClass__radius
