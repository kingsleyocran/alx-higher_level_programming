#!/usr/bin/python3
""" Module Square"""


class Square:
    """Represents a square.
    - Private instance attribute: size:
        - property def size(self)
        - property setter def size(self, value)
    - Private instance attribute: position:
        - property def position(self)
        - property setter def position(self, value)
    - Instantiation with optional size and optional position.
    - Public instance method: def area(self).
    - Public instance method: def my_print(self).
    Attributes:
        size (int): Size of square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes method
        Args:
            size (int): size of a side of the square
            postion(tuple): postion of square in 2D space
        Returns:
            None
        """
        self.__size = size
        self.__position = position

    def __str__(self):
        """Str method for print from main module."""
        my_str = ""
        if self.__size == 0:
            return ''
        else:
            my_str += '\n' * self.__position[1]
            for i in range(0, self.__size):
                my_str += ' ' * self.__position[0]
                my_str += '#' * self.__size
                my_str += '\n'
            return my_str[:-1]

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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get postion attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
            setter of position
        Args:
            value (tuple): position of the square in 2D space
        Returns:
            None
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square
        Return:
            int: Current square area
        """
        return self.__size ** 2

    def my_print(self):
        """Print a square from the size using #
        Returns:
            None
        """
        if self.__size == 0:
            print()
        else:
            for y in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                for x in range(0, self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print()
            return ''
