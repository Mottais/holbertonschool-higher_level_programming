#!/usr/bin/python3
"""contient la fonction class_to_json """


def class_to_json(obj):
    """return  dictionnaire contenant les attributs de l'objet obj
    'attribut' : valeur
    """
    return obj.__dict__
