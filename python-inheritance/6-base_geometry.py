#!/usr/bin/python3
""" Définition de la classe BaseGemotry"""


class BaseGeometry:
    """Classe vide"""
    def area(self):
        """méthode non implémentée"""
        raise Exception("area() is not implemented")


bg = BaseGeometry()
