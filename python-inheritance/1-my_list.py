#!/usr/bin/python3
"""Ce module définit une classe MyList
qui hérite de la classe list de Python.
Cette classe ajoute une méthode supplémentaire
print_sorted() qui imprime les éléments de la liste triée.
"""


class MyList(list):
    """Classe héritant de list
    avec une méthode supplémentaire
    pour imprimer les éléments triés.
    """
    def print_sorted(self):
        """Méthode pour imprimer les éléments
        de la liste triés par ordre croissant.

        Args:
            Aucun

        Returns:
            Aucun
        """
        for element in self:
            if type(element) is not int:
                raise TypeError("toto")
        print(sorted(self))
