#!/usr/bin/python3
"""Class Rectangle inherit from Base"""


from models.base import Base


class Rectangle(Base):
    """Class Rectangle inherit Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        attributes = ["width", "height", "x", "y"]
        for attr in attributes:
            value = locals()[attr]
            if not isinstance(value, int):
                raise TypeError(f"{attr} must be an integer")
            elif (attr == "width" or attr == "height") and value <= 0:
                raise ValueError(f"{attr} must be > 0")
            elif (attr == "y" or attr == "x") and value < 0:
                raise ValueError(f"{attr} must be >= 0")
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not type(value) is int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not type(value) is int:
            raise TypeError("y must be an integer")
        if int(value) < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return area of rectangle"""
        return self.__height * self.__width

    def display(self):
        """Print with #"""
        print("{}".format("\n" * self.__y), end="")
        print(
            "{}".format("\n".join(
                [" " * self.__x + "#" * self.__width] * self.__height)))

    def __str__(self):
        """definition of str for print"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """Definition update with variadic function"""
        if args:
            i = 0
            listme = ["id", "width", "height", "x", "y"]
            for arg in args:
                setattr(self, listme[i], arg)
                i += 1
            return
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """return dict representation of Rectangle"""
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width,
        }
