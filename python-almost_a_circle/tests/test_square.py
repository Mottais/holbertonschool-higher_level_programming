#!/usr/bin/python3
import unittest
import sys
from models.square import Square
from models.base import Base
from io import StringIO
"""Runs test cases for the Rectangle module"""


class test_rectangle(unittest.TestCase):
    """Testing rectangle"""
    def test_01_init_(self):
        """Testing _init"""
        Base._Base__nb_objects = 0
        sq1 = Square(10)
        sq2 = Square(10, 2, 3, 12)
        self.assertTrue(sq1.size == 10)
        self.assertTrue(sq1.width == 10)
        self.assertTrue(sq1.height == 10)
        self.assertTrue(sq2.x == 2)
        self.assertTrue(sq2.y == 3)

    def test_02_str(self):
        """Testing __str__"""
        sq = Square(4, 2, 1, 12)
        self.assertTrue(str(sq) == "[Square] (12) 2/1 - 4")

    def test_03_update(self):
        """Testing update"""
        sq = Square(1, 2, 3, 4)
        sq.update(1, 2, 3, 4)
        self.assertTrue(str(sq) == "[Square] (1) 3/4 - 2")

    def test_04_to_dictionary(self):
        """Testing to_dictionary"""
        sq = Square(1, 2, 3, 4)
        self.assertTrue(sq.to_dictionary() == {'x': 2, 'y': 3, 'id': 4, 'size': 1})

    if __name__ == '__main__':
        unittest.main()
