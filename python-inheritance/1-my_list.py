#!/usr/bin/python3
"""
Mododul containt :
class MyList that inherits list
"""


class MyList(list):
    """
    class MyList that inherits from list
    """
    def print_sorted(self):
        """
        fonction qui imprime la l'objet trié
        """
        print(sorted(self))
