#!/usr/bin/python3
""" Définition de la classe BaseGemotry"""


class BaseGeometry:
    """Classe BaseGeometry contenant les méthodes d'instance publique :
    -area
    -integer_validator
    """
    def area(self):
        """méthode non implémentée"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """méthode qui teste valeur (nommé name) si
        - est un int
        - et > 0
        """
        if type(name) is not str:
            raise TypeError("toto")
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
