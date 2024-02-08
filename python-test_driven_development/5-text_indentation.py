#!/usr/bin/python3
""" Prints a text with 2 new lines
after each of these characters: ., ? and :
text must be a string,
There should be no space at the beginning
or at the end of each printed line"""


def text_indentation(text):
    """ Prints a text with 2 new lines
    after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0
    while i < (len(text)):
        print(text[i], end="")
        if text[i] in '.?:':
            print("\n")
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        i += 1
