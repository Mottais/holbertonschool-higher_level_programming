#!/usr/bin/python3
"""Ce module définit la fonction 'is_same_class'
qui teste si l'objet est une instance de la classe spécifiée
"""


def is_same_class(obj, a_class):
    """qui renvoie  spécifiée ; sinon False.
    Args:
        obj: objet à tester
        a_class: classe spécifiée

    Returns:
        True: si l'obj est une instance de a_class
        False: sinon
    """
    return type(obj) is a_class
