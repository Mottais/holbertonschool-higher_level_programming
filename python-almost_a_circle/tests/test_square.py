#!/usr/bin/python3
import unittest, os, sys, json
from models.square import Square
from models.base import Base
from io import StringIO
"""Runs test cases for the square module"""


class test_square(unittest.TestCase):
    """Testing square"""

    def test_asquare_id(self):
        """Test the id for square"""
        sq = Square(2, 0, 0, 199)
        self.assertEqual(199, sq.id)

    def test_width_string(self):
        """Testing for other than int"""
        with self.assertRaises(TypeError):
            sq = Square("1")

    def test_x_string(self):
        """Testing for other than int"""
        with self.assertRaises(TypeError):
            sq = Square(1, "46")

    def test_y_string(self):
        """Testing for other than int"""
        with self.assertRaises(TypeError):
            sq = Square(1, 7, "46")

    def test_width_negative(self):
        """Testing with negative int"""
        with self.assertRaises(ValueError):
            sq = Square(-4)

    def test_x_negative(self):
        """Testing with negative int"""
        with self.assertRaises(ValueError):
            sq = Square(4, -3)

    def test_y_negative(self):
        """Testing with negative int"""
        with self.assertRaises(ValueError):
            sq = Square(4, 2, -3)

    def test_width_zero(self):
        """Testing with negative int"""
        with self.assertRaises(ValueError):
            sq = Square(0, 5)








    def test_str_overload(self):
        s = Square(5, 8, 7, 88)
        self.assertEqual(s.__str__(), "[Square] (88) 8/7 - 5")











    def test_saving_to_file_None(self):
        """Testing saving a file into json format sending None"""
        try:
            os.remove("Square.json")
        except:
            pass
        r1 = Square(5, 0, 0, 346)
        Square.save_to_file(None)

        with open("Square.json", "r") as file:
            content = file.read()

        self.assertEqual("[]", content)




    '''def test_load_from_file_same_width(self):
        """Checking that an object was created from the
        list and has the same witdh"""
        r1 = Square(10)
        list_squares_input = [r1]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(r1.width, list_squares_output[0].size)'''

    def test_load_from_file_same_height(self):
        """Checking that an object was created from the
        list and has the same height"""
        r1 = Square(10)
        list_squares_input = [r1]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(r1.size, list_squares_output[0].size)

    def test_load_from_file_same_x(self):
        """Checking that an object was created from the
        list and has the same x"""
        r1 = Square(10, 2, 8)
        list_squares_input = [r1]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(r1.x, list_squares_output[0].x)

    def test_load_from_file_same_y(self):
        """Checking that an object was created from the
        list and has the same y"""
        r1 = Square(10, 2, 8)
        list_squares_input = [r1]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(r1.y, list_squares_output[0].y)

    def test_display_square(self):
        """Checking the stdout output by capturing it"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Square(10)
        r1.display()
        sys.stdout = sys.__stdout__
        output = (
            "##########\n"
            + "##########\n"
            + "##########\n"
            + "##########\n"
            + "##########\n"
            + "##########\n"
            + "##########\n"
            + "##########\n"
            + "##########\n"
            + "##########\n"
        )
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_display_square_size_one(self):
        """Checking the stdout output by capturing it"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Square(1)
        r1.display()
        sys.stdout = sys.__stdout__
        output = "#\n"
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_display_square_size_zero(self):
        """Checking the stdout output by capturing it"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Square(3)
        r1.display()
        sys.stdout = sys.__stdout__
        output = "###\n###\n###\n"
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_display_square(self):
        """Checking the stdout output by capturing it"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Square(10)
        r1.display()
        sys.stdout = sys.__stdout__
        output = (
            "##########\n"
            + "##########\n"
            + "##########\n"
            + "##########\n"
            + "##########\n"
            + "##########\n"
            + "##########\n"
            + "##########\n"
            + "##########\n"
            + "##########\n"
        )
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_display_square_size_one(self):
        """Checking the stdout output by capturing it"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Square(1)
        r1.display()
        sys.stdout = sys.__stdout__
        output = "#\n"
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_display_square_size_zero(self):
        """Checking the stdout output by capturing it"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Square(3)
        r1.display()
        sys.stdout = sys.__stdout__
        output = "###\n###\n###\n"
        self.assertEqual(capturedOutput.getvalue(), output)

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
