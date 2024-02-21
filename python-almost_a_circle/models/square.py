#!/usr/bin/python3
"""define a class inheriting from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """define a class inheriting from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square's position
            y (int, optional): The y-coordinate of the square's position
            id (int, optional): The unique identifier of the square
        """
        super().__init__(size, size, x, y, id)
        # ou bien
        # Rectangle.__init__(self, size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the Square."""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}")

    def update(self, *args, **kwargs):
        """
        Update value of Square object
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
                if len(args) > 1:
                    self.size = args[1]
                    if len(args) > 2:
                        self.x = args[2]
                        if len(args) > 3:
                            self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Square."""
        return dict(id=self.id, x=self.x, size=self.size, y=self.y)
