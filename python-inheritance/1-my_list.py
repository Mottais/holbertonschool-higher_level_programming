#!/usr/bin/python3
"""
Mododule contenant :
class MyList MyList qui hérite de la class list
avec fonction qui imprime l'objet trié
"""


class MyList(list):
    """
    class qui hérite de la class list
    """
    def print_sorted(self):
        """
        fonction qui imprime l'objet trié
        """
        print(sorted(self))
