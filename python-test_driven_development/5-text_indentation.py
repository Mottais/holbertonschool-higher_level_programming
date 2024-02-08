#!/usr/bin/python3
"""
this
is a
5 line comment
"""


def text_indentation(text):
    """
    indenting a text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print(text[i], end='')
        if text[i] in ".?:":
            print("\n")
            while (i + 1 < len(text) and text[i + 1] == ' '):
                i += 1
        i += 1
