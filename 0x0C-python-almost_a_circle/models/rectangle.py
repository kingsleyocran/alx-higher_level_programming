#!/usr/bin/python3
'''
    Rectangle Class
'''
from models.base import Base


class Rectangle(Base):
    '''
        Defining the Rectangle class
        Inherits from:
            Base
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''
            Getter method for width
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
            Setter method for width
        '''
        self.__width = value

    @property
    def height(self):
        '''
            Getter method for height
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
            Setter method for height
        '''
        self.__height = value


