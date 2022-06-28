#!/usr/bin/python3
"""Module 5-rectangle
Defines a Rectangle class.
"""


class Rectangle:
    """Rectangle class defined by geometric shap
     - Instantiation with size (no type/value verification).
    Instance Attributes:
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
        self.__width = width

        #: int: height attribute for height
        self.__height = height

    def __str__(self):
        """Returns an informal and nicely printable string representation
        of a Rectangle instance, filled with the '#' character."""

        if self.__height == 0 or self.__width == 0:
            return ''

        rec_str = ''

        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += '#'
            rec_str += '\n'

        return rec_str[:-1]

    def __repr__(self):
        """Return a string representation of a Rectangle instance
        that is able to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Delete method."""
        print("Bye rectangle...")

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

    def area(self):
        """Calculates the area of a Rectangle instance
        Returns:
            Area of the the rectangle, given by height * width
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of a Rectangle instance
        Returns:
            Perimeter of the rectangle, given by 2 * (height + width)
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
