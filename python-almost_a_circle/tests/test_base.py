#!/usr/bin/python3
import unittest
import json
from models.base import Base

from models.square import Square
"""Creating test cases for the base module"""


class test_base(unittest.TestCase):
    """Testing base"""

    def test_init_(self):
        """création d'un objet de la classe Base"""
        b = Base()
        self.assertTrue(b.id == 1)
        b = Base()
        self.assertTrue(b.id == 2)
        b = Base(1)
        self.assertTrue(b.id == 1)
        b = Base()
        self.assertTrue(b.id == 3)
        b = Base(4)
        self.assertTrue(b.id == 4)
        b = Base()
        self.assertTrue(b.id == 4)
        b = Base(-20)
        self.assertTrue(b.id == -20)
        b = Base("Betty")
        self.assertTrue(b.id == "Betty")
        b = Base([1, 2, 3])
        self.assertTrue([1, 2, 3] == b.id)
        b = Base({"id": 109})
        self.assertTrue({"id": 109} == b.id)

    def test_init_ZeroDivisionError(self):
        """Creating a Base object with a division by zero"""
        with self.assertRaises(ZeroDivisionError):
            b = Base(1/0)
            print(b)

    def test_init_TypeError(self):
        """Creating a Base object with a TypeError"""
        with self.assertRaises(TypeError):
            b = Base(1, 1)
            print(b)

    '''def test_init_ValueError(self):
        """Creating a Base object with a TypeError"""
        with self.assertRaises(ValueError):
            b = Base(int("9" * 4301))
            print(b)'''

    def test_to_json_type(self):
        """Testing the json string"""
        sq = Square(1)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertTrue(type(json_string) is str)

        Dict = {"toto": "tutu"}
        json_string = Base.to_json_string([Dict, Dict])
        self.assertTrue(json_string == '[{"toto": "tutu"}, {"toto": "tutu"}]')
        self.assertTrue(type(json_string) is str)

        json_string = Base.to_json_string(1)
        self.assertTrue(json_string == '1')
        self.assertTrue(type(json_string) is str)

        json_string = Base.to_json_string(None)
        self.assertTrue(json_string == '[]')
        self.assertTrue(type(json_string) is str)

        json_string = Base.to_json_string([])
        self.assertTrue(json_string == '[]')
        self.assertTrue(type(json_string) is str)

    def test_to_json_value(self):
        """Testing the json string"""
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertTrue(
            json.loads(json_string) == [{"id": 609, "y": 0, "size": 1, "x": 0}]
        )

    def test_to_json_None(self):
        """Testing the json string"""
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string(None)
        self.assertTrue(json_string == "[]")

    def test_to_json_Empty(self):
        """Testing the json string"""
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([])
        self.assertTrue(json_string == "[]")


if __name__ == '__main__':
    unittest.main()
