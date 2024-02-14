#!/usr/bin/python3
""" Définition de la classe BaseGemotry"""


class BaseGeometry:
    """Classe vide"""
    def area(self):
        """méthode non implémentée"""
        raise Exception("area() is not implemented")


bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
