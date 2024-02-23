#!/usr/bin/python3
import unittest
import os
import json
import sys
from models.rectangle import Rectangle, Base
from io import StringIO
"""Runs test cases for the Rectangle module"""


class test_rectangle(unittest.TestCase):
    """Testing rectangle"""
    def test_01_init_(self):
        """Testing _init"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 2)
        r2 = Rectangle(10, 2, 3, 4, 12)
        self.assertTrue(r1.width == 10)
        self.assertTrue(r1.height == 2)
        self.assertTrue(r2.x == 3)
        self.assertTrue(r2.y == 4)

    def test_02_init_TypeError(self):
        """Creating a Rectangle object with a TypeError"""
        with self.assertRaises(TypeError):
            r = Rectangle("1", 1)
            print(r)

    def test_03_init_ValueError(self):
        """Creating a Rectangle object with a ValueError"""
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 1)
            print(r)

    def test_04_init_ZeroDivisionError(self):
        """Creating a Rectangle object with a division by zero"""
        with self.assertRaises(ZeroDivisionError):
            r = Rectangle(1/0, 2)
            print(r)

    def test_05_area(self):
        """Testing area"""
        r1 = Rectangle(3, 2)
        self.assertTrue(r1.area() == 6)

    def test_06_display(self):
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
        self.assertEqual(output.getvalue(), "##\n" * 3)

    def test_07_str(self):
        """Testing __str__"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertTrue(str(r1) == "[Rectangle] (12) 2/1 - 4/6")

    def test_08_update(self):
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
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")

    '''
    def test_11_save_to_file(self): # 14
        """Testing save_to_file"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(json.loads(file.read()), [r1.to_dictionary(),
                                                       r2.to_dictionary()])

    def test_14_save_to_file_None(self): # 18
        """Testing save_to_file None"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_15_load_from_file_None(self): # 19
        """Testing load_from_file None"""
        list_output = Rectangle.load_from_file()
        self.assertEqual(list_output, [])

    def test_16_save_to_file_empty(self): # 20
        """Testing save_to_file empty"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_17_load_from_file_empty(self): # 21
        """Testing load_from_file empty"""
        list_output = Rectangle.load_from_file()
        self.assertEqual(list_output, [])

    def test_19_load_from_file_no_file(self): # 23
        """Testing load_from_file no file"""
        os.remove("Rectangle.json")
        list_output = Rectangle.load_from_file()
        self.assertEqual(list_output, [])
    '''

    if __name__ == '__main__':
        unittest.main()
