#!/usr/bin/python3
"""Module 1-rectangle
Defines a Rectangle class.
"""


class Rectangle:
    """Rectangle class defined by geometric shap
     - Instantiation with size (no type/value verification).
    Attributes:
        width (int): The width of the new rectangle.
        height (int): The height of the new rectangle.
    """

    def __init__(self, width=0, height=0):
        """Initialize method
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """

        #: int: width attribute for width
        self.width = width

        #: int: height attribute for height
        self.height = height

    @property
    def width(self):
        """Getter for the width of the rectangle."""

        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width of the rectangle."""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the width of the rectangle."""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
