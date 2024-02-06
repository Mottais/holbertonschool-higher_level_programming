#!/usr/bin/python3
"""
print_square function
prints a square with the character #.
Retunr error if :
size is not in
size < 0
"""


def print_square(size):
    """
    print a square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print(("#" * size + "\n") * size, end="")
