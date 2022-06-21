#!/usr/bin/python3
""" Module Square"""


class Square:
    """Represents a square.
    - Private instance attribute: size:
        - property def size(self)
        - property setter def size(self, value)
    - Instantiation with optional size.
    - Public instance method: def area(self).
    Attributes:
        size (int): Size of square
    """

    def __init__(self, size=0):
        """iInitializes method
        Args:
            size (int): size of a side of the square
        Returns:
            None
        """
        self.__size = size

    def __eq__(self, other):
        """Equal."""
        if hasattr(other, 'size'):
            return self.__size == other.__size
        return self.__size == other

    def __ne__(self, other):
        """Not equal."""
        return not self.__eq__(other)

    def __lt__(self, other):
        """Less than."""
        if hasattr(other, 'size'):
            return self.__size < other.__size
        return self.__size < other

    def __le__(self, other):
        """Less than or equal."""
        if hasattr(other, 'size'):
            return self.__size <= other.__size
        return self.__size <= other

    @property
    def size(self):
        """
        getter of size
        Return:
            Size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter of size
        Args:
            value (int): size of a side of the square
        Raises
            TypeError: if size is not int
            ValueError: size less than 0
        Returns:
            None
        """
        if not isinstance(value, int) or not isinstance(value, float):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square
        Return:
            Current square area (int)
        """
        return self.__size ** 2


"""
s_5 = Square(5)
s_6 = Square(6)

if s_5 < s_6:
    print("Square 5 < Square 6")
if s_5 <= s_6:
    print("Square 5 <= Square 6")
if s_5 == s_6:
    print("Square 5 == Square 6")
if s_5 != s_6:
    print("Square 5 != Square 6")
if s_5 > s_6:
    print("Square 5 > Square 6")
if s_5 >= s_6:
    print("Square 5 >= Square 6")
"""
