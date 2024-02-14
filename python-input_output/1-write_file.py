#!/usr/bin/python3
"""Definition of write function"""


def write_file(filename="", text=""):
    """ function that writes a string to a text file (UTF8)  """
    with open(filename, "w", encoding='utf-8') as file:
        return file.write(text)
