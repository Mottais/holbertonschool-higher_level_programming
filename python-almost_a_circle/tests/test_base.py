#!/usr/bin/python3
import unittest
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

    def test_to_json_string(self):
        """Testing the json string"""

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

    def test_to_json_string_TypeError(self):
        """using to_json_string with a TypeError"""
        with self.assertRaises(TypeError):
            json_string = Base.to_json_string()
            print(json_string)

    def test_from_json_string(self):
        """Testing from_json_string"""

        String_liste = '[{"toto": 1}, {"tutu": 2}]'
        obj_from_sting = Base.from_json_string(String_liste)
        self.assertTrue((obj_from_sting == [{"toto": 1}, {"tutu": 2}]))
        self.assertTrue(type(obj_from_sting) is list)

        String_liste = None
        obj_from_sting = Base.from_json_string(String_liste)
        self.assertTrue((obj_from_sting == []))
        self.assertTrue(type(obj_from_sting) is list)

        String_liste = '[]'
        obj_from_sting = Base.from_json_string(String_liste)
        self.assertTrue((obj_from_sting == []))
        self.assertTrue(type(obj_from_sting) is list)

        String_liste = '1'
        obj_from_sting = Base.from_json_string(String_liste)
        self.assertTrue((obj_from_sting != []))
        self.assertTrue(type(obj_from_sting) is not list)

    def test_from_json_string_TypeError(self):
        """using from_json_string with a TypeError"""
        with self.assertRaises(TypeError):
            String = 2
            obj_from_sting = Base.from_json_string(String)
            print(obj_from_sting)

    def test_save_to_file(self):
        """Testing save_to_file"""

        sq1 = Square(1)
        sq2 = Square(2)
        Base.save_to_file( [sq1, sq2])
        with open("Base.json", "r") as file:
            self.assertTrue(type(file.read()) is str)

        Base.save_to_file(None)
        with open("Base.json", "r") as file:
            File_contain = (file.read())
            self.assertTrue(File_contain == "[]")

        Base.save_to_file([])
        with open("Base.json", "r") as file:
            File_contain = (file.read())
            self.assertTrue(File_contain == "[]")


if __name__ == '__main__':
    unittest.main()
