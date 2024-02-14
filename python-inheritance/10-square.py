#!/usr/bin/python3
""" Définition de la classe Square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Classe Square herite de la classe Rectangle"""
    def __init__(self, size):
        "teste et initialise l'attributs size"
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        # ou
        # super().__init__(size, size)
