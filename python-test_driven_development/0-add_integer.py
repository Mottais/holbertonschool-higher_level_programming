#!/usr/bin/python3
""" Return the addition of two integer
>>> add_integer(5, 10)
15
>>> add_integer(2)
100"""


def add_integer(a, b=98):
    """Computes the sum of two integers
        return error if a or b is not integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    add = int(a) + int(b)
    return add
