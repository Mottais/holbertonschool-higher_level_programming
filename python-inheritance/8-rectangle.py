#!/usr/bin/python3
""" Définition de la classe BaseGemotry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Classe Retangle herite de la classe BaseGeometry"""
    def __init__(self, width, height):
        "teste et initialise les attributs __width et __height"
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
