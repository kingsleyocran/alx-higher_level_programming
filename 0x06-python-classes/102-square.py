#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.__size = size

    def __eq__(self, other):
        if hasattr(other, 'size'):
            return self.__size == other.__size
        return self.__size == other

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if hasattr(other, 'size'):
            return self.__size < other.__size
        return self.__size < other

    def __le__(self, other):
        if hasattr(other, 'size'):
            return self.__size <= other.__size
        return self.__size <= other

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int) or not isinstance(value, float):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
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