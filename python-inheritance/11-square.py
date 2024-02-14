#!/usr/bin/python3
""" Définition de la classe Square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Classe Square herite de la classe Rectangle"""
    def __init__(self, size):
        "teste et initialise l'attributs size"
        Rectangle.__init__(self, size, size)
        self.__size = size

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
