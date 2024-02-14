#!/usr/bin/python3
"""Ce module définit la fonction 'is_kind_of_class'
qui teste
si l'objet est une instance de,
ou
si l'objet est une instance d'une classe qui a hérité de,
la classe spécifiée
"""


def is_kind_of_class(obj, a_class):
    """Teste l'instance de obj
    Args:
        obj: objet à tester
        a_class: classe spécifiée

    Returns:
        True: si l'obj est une instance de a_class
        False: sinon
    """
    return type(obj) is a_class
