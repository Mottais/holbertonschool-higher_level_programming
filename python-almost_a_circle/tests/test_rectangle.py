#!/usr/bin/python3
import unittest
import sys
from models.rectangle import Rectangle, Base
from io import StringIO
"""Runs test cases for the Rectangle module"""


class test_rectangle(unittest.TestCase):
    """Testing rectangle"""
    '''def test_01_init_(self):
        """Testing _init"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 2)
        r2 = Rectangle(10, 2, 3, 4, 12)
        self.assertTrue(r1.width == 10)
        self.assertTrue(r1.height == 2)
        self.assertTrue(r2.x == 3)
        self.assertTrue(r2.y == 4)'''

    '''def test_02_init_TypeError(self):
        """Creating a Rectangle object with a TypeError"""
        with self.assertRaises(TypeError):
            r = Rectangle("1", 1)
            print(r)'''

    '''def test_03_init_ValueError(self):
        """Creating a Rectangle object with a ValueError"""
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 1)
            print(r)'''

    '''def test_04_init_ZeroDivisionError(self):
        """Creating a Rectangle object with a division by zero"""
        with self.assertRaises(ZeroDivisionError):
            r = Rectangle(1/0, 2)
            print(r)'''

    '''def test_05_area(self):
        """Testing area"""
        r1 = Rectangle(3, 2)
        self.assertTrue(r1.area() == 6)'''

    '''def test_06_display(self):
        """Testing display"""
        r1 = Rectangle(2, 3)

        # objet StringIO, qui est essentiellement un fichier
        # en mémoire utilisé pour capturer la sortie standard.
        output = StringIO()

        # redirige la sortie standard (stdout) vers l'objet output,de sorte
        # que toute sortie imprimée avec print sera capturée par cet objet.
        sys.stdout = output
        r1.display()

        # réinitialise la sortie standard à sa valeur par défaut.
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "##\n" * 3)'''

    '''def test_07_str(self):
        """Testing __str__"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertTrue(str(r1) == "[Rectangle] (12) 2/1 - 4/6")'''

    '''def test_08_update(self):
        """Testing update"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")
        r1.update(89, 2, 3, 4, 5, 6)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")'''

    '''if __name__ == '__main__':
        unittest.main()'''
    pass


from models.square import Square
import os


class test_square(unittest.TestCase):
    """Testing square"""

    def test_width_string(self):
        """Testing for other than int"""
        with self.assertRaises(TypeError):
            sq = Rectangle("1")
        with self.assertRaises(TypeError):
            sq = Square(1, "46")
        with self.assertRaises(TypeError):
            sq = Square(1, 7, "46")

    def test_width_negative(self):
        """Testing with negative int"""
        with self.assertRaises(ValueError):
            sq = Square(-4)
        with self.assertRaises(ValueError):
            sq = Square(4, -3)
        with self.assertRaises(ValueError):
            sq = Square(4, 2, -3)
        with self.assertRaises(ValueError):
            sq = Square(0)

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

        self.assertTrue("[]" == content)

    def test_load_from_file_same_y(self):
        """Checking that an object was created from the
        list and has the same y"""
        r1 = Square(10, 2, 8)
        list_squares_input = [r1]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertTrue(r1.y == list_squares_output[0].y)

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
