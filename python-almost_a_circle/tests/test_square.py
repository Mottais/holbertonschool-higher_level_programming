#!/usr/bin/python3
import unittest
import os
import sys
from models.square import Square
from io import StringIO
"""Runs test cases for the square module"""


class test_square(unittest.TestCase):
    """Testing square"""

    def test_01_init_(self):
        """Testing _init"""
        sq = Square(2, 0, 0, 199)
        self.assertTrue(199 == sq.id)

    def test_02_init_TypeError(self):
        """Creating a Square object with a TypeError"""
        with self.assertRaises(TypeError):
            Square([1, 2])
        with self.assertRaises(TypeError):
            Square(1, (2,))
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_03_init_ValueError(self):
        """Creating a Square object with a ValueError"""
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(ValueError):
            Square(0)

    def test_display_square_size_zero(self):
        """Checking the stdout output by capturing it"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Square(3)
        r1.display()
        sys.stdout = sys.__stdout__
        output = "###\n###\n###\n"
        self.assertTrue(capturedOutput.getvalue() == output)


if __name__ == '__main__':
    unittest.main()
