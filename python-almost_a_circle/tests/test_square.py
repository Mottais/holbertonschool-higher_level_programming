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

    def test_saving_to_file_None(self):
        """Testing saving a file into json format sending None"""
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertTrue(file.read() == "[]")

    def test_load_from_file_same_y(self):
        """Checking that an object was created from the
        list and has the same y"""
        '''with open("Square.json", "w") as file:
            file.write('[{"id": 1, "x": 2, "size": 1, "y": 3}]')'''
        sq = Square(1, 2, 3)
        list_squares_input = [sq]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertTrue(type(list_squares_output[0]) is type(sq))
        self.assertTrue(sq.y == list_squares_output[0].y)

    def test_display_square_size_zero(self):
        """Checking the stdout output by capturing it"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Square(3)
        r1.display()
        sys.stdout = sys.__stdout__
        output = "###\n###\n###\n"
        self.assertTrue(capturedOutput.getvalue() == output)

    def test_saving_to_file_empty_list(self):
        """Test saving a file into JSON format with an empty list"""
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass
        # Create an instance of your Square class
        square = Square(5, 0, 0, 346)
        # Call the save_to_file method with an empty list
        square.save_to_file([])
        # You can add assertions to verify the test's success, for example, checking if the file exists
        self.assertTrue(os.path.exists("Square.json"))

    if __name__ == '__main__':
        unittest.main()
