#!/usr/bin/python3
"""Contains an class : 'Square'"""


class Square:
    """A class representing a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the Square with a given size."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not type(value) is int:
            raise Exception("size must be an integer")
        if value < 0:
            raise Exception("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """Set the position of the square."""
        cond1 = type(value) is tuple and len(value) == 2
        cond2 = type(value[0]) is int and type(value[1]) is int
        cond3 = value[0] >= 0 and value[1] >= 0
        if cond1 and cond2 and cond3:
            self.__position = value
        else:
            raise Exception("position must be a tuple of 2 positive integers")

    def area(self):
        """Return square of size"""
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        else:
            print("\n" * self.position[1], end='')
            for _ in range(self.size):
                print(" " * self.position[0], "#" * self.size, sep='')
