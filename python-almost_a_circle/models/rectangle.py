#!/usr/bin/python3
"""define a class inheriting from Base"""
from models.base import Base


class Rectangle(Base):
    """define a class inheriting from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position
            y (int, optional): The y-coordinate of the rectangle's position
            id (int, optional): The unique identifier of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @property
    def x(self):
        """Get the position x of the rectangle."""
        return self.__x

    @property
    def y(self):
        """Get the position y of the rectangle."""
        return self.__y

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Set the position x of the rectangle."""
        if not type(value) is int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Set the position y of the rectangle."""
        if not type(value) is int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Print the rectangle with the character #."""

        Rec_prt = (((" " * self.__x + "#" * self.__width+'\n')
                    * self.__height)[:-1])
        print("\n" * self.__y + Rec_prt)

    def __str__(self):
        """Return a string representation of the rectangle."""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
                f"{self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """
        Update value of Rectangle object
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
                if len(args) > 1:
                    self.__width = args[1]
                    if len(args) > 2:
                        self.__height = args[2]
                        if len(args) > 3:
                            self.x = args[3]
                            if len(args) > 4:
                                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return dict(x=self.x, y=self.y, id=self.id,
                    width=self.width, height=self.height)
