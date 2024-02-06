#!/usr/bin/python3
"""Defines say_my_name function"""


def say_my_name(first_name, last_name=""):
    """Prints 'My name is <first name> <last name>'
        TypeError: The first_name or last_name is not a string
    """
    if not type(first_name) is str:
        raise TypeError("first_name must be a string")
    if not type(last_name) is str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
