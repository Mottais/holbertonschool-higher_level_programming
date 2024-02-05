class Square:
    """A class representing a square."""

    def __init__(self, size=0):
        """Initialize the Square with a given size."""
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not type(value) is int:
            raise Exception("Size must be an integer")
        if value < 0:
            raise Exception("Size must be >= 0")
        self.__size = value

    def area(self):
        """Return square of size"""
        return self.__size ** 2
