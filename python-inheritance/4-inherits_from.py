#!/usr/bin/python3
"""Ce module définit la fonction 'inherits_from'
qui vérifie si l'objet est une instance d'une classe
qui a hérité (directement ou indirectement)
de la classe spécifiée.
"""


def inherits_from(obj, a_class):
    """
    Vérifie si l'objet est une instance d'une classe
    qui a hérité (directement ou indirectement)
    de la classe spécifiée.

    Args:
    - obj: L'objet à vérifier.
    - a_class: La classe parente à vérifier.

    Returns:
    - True si obj est une instance d'une sous-classe de a_class
      sinon False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
