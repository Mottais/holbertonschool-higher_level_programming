#!/usr/bin/python3
'''
Module Contains class definition of 'Rectangle'
'''


class Rectangle:
    '''
    class Rectangle that defines a rectangle
    '''
    def __init__(self, width=0, height=0):
        """Initialize the Rectangle with a given width and height."""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
