#!/usr/bin/python3
"""
class MyList that inherits from list
fonction qui imprime la l'objet trié
"""


class MyList(list):
    """fonction qui imprime la l'objet trié"""
    def print_sorted(self):
        print(sorted(self))
