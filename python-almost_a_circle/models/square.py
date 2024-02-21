#!/usr/bin/python3
"""

A class Square that inherits from Rectangle

"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class Square that inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the Square"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """def in str format for print"""
        return ("[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """Update value of attribute"""
        if args:
            list_arg = ["id", "size", "x", "y"]
            i = 0
            for attr in args:
                setattr(self, list_arg[i], attr)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
