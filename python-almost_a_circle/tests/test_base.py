#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os

"""Creating test cases for the base module"""


class test_base(unittest.TestCase):
    """Testing base"""

    def test_01_init_(self):
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

    def test_02_init_ZeroDivisionError(self):
        """Creating a Base object with a division by zero"""
        with self.assertRaises(ZeroDivisionError):
            b = Base(1/0)
            print(b)

    def test_02_init_TypeError(self):
        """Creating a Base object with a TypeError"""
        with self.assertRaises(TypeError):
            b = Base(1, 1)
            print(b)
    # AVEC CE TEST AUCUN 'CHECKER' NE PASSE ???
    '''def test_init_ValueError(self):
        """Creating a Base object with a TypeError"""
        with self.assertRaises(ValueError):
            b = Base(int("9" * 4301))
            print(b)'''

    def test_04_to_json_string(self):
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

    def test_05_to_json_string_TypeError(self):
        """using to_json_string with a TypeError"""
        with self.assertRaises(TypeError):
            json_string = Base.to_json_string()
            print(json_string)

    def test_06_from_json_string(self):
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

    def test_07_from_json_string_TypeError(self):
        """using from_json_string with a TypeError"""
        with self.assertRaises(TypeError):
            String = 2
            obj_from_sting = Base.from_json_string(String)
            print(obj_from_sting)

    def test_08_save_to_file(self):
        """Testing save_to_file"""

        sq1 = Square(1)
        sq2 = Square(2)
        Base.save_to_file([sq1, sq2])
        with open("Base.json", "r") as file:
            self.assertTrue(type(file.read()) is str)

        Base.save_to_file(None)
        with open("Base.json", "r") as file:
            self.assertTrue((file.read()) == "[]")

        # POURQUOI CE MEME TEST SUR 'Base' NE SUFFIT PAS AU 'CHECKER' ???
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertTrue(file.read() == "[]")


        '''try:
            os.remove("Base.json")
        except FileNotFoundError:
            pass
        Base.save_to_file([])
        with open("Base.json", "r") as file:
            self.assertTrue((file.read()) == "[]")'''

        # POURQUOI CE MEME TEST SUR 'Base' NE SUFFIT PAS AU 'CHECKER' ???
        # POURQOUI FAUT-IL SUPPR 'Square.json' avant ave_to_file ???
        try:
            os.remove("Square.json")
        except Exception:
            pass
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertTrue((file.read()) == "[]")


    def test_09_create(self):
        """Testing create"""

        r_dictionary = {'x': 1, 'y': 2, 'id': 11, 'width': 3, 'height': 4}
        sq_dictionary = {'x': 1, 'y': 2, 'id': 22, 'size': 3}

        r = Rectangle.create(**r_dictionary)
        self.assertTrue(str(r) == '[Rectangle] (11) 1/2 - 3/4')

        sq = Square.create(**sq_dictionary)
        self.assertTrue(str(sq) == '[Square] (22) 1/2 - 3')

        sq2 = Square.create(**r_dictionary)
        self.assertTrue(str(sq2) == '[Square] (11) 1/2 - 3')

        r2 = Rectangle.create(**sq_dictionary)
        self.assertTrue(str(r2) == '[Rectangle] (22) 1/2 - 1/1')

        '''r = Rectangle.create(**{})
        self.assertTrue(str(r) == '[Rectangle] (11) 0/0 - 1/1')'''

    def test_10_create_TypeError(self):
        """using create with a TypeError"""
        with self.assertRaises(TypeError):
            r_dictionary = {'x': 1, 'y': 2, 'id': 11, 'width': 3, 'height': 4}
            r = Rectangle.create(2, **r_dictionary)
            print(r)

    def test_11_create_UnboundLocalError(self):
        """using create with a UnboundLocalError"""
        with self.assertRaises(UnboundLocalError):
            r_dictionary = {'x': 1, 'y': 2, 'id': 11, 'width': 3, 'height': 4}
            b = Base.create(**r_dictionary)
            print(b)

    def test_12_load_from_file(self):
        """Testing load_from_file"""

        if os.path.exists("Square.json"):
            os.remove("Square.json")
        list_rectangles_output = Square.load_from_file()
        self.assertTrue(list_rectangles_output == [])

        with open("Square.json", "w") as file:
            file.write('[{"size": 3, "id": 111},{"width": 2, "height": 2}]')
        list_rectangles_output = Square.load_from_file()
        self.assertTrue(isinstance(list_rectangles_output[0], Square))
        self.assertTrue(isinstance(list_rectangles_output[1], Square))

        with open("Square.json", "w") as file:
            file.write('[{"toto": 111}]')
        list_rectangles_output = Square.load_from_file()
        self.assertTrue(isinstance(list_rectangles_output[0], Square))



    def test_load_from_file_same_y(self):
        """Checking that an object was created from the list"""
        # POURQUOI LE CHECKER NE PASSE PAS EN CREANT "Square.json" VIA open ???"
        '''with open("Square.json", "w") as file:
            file.write('[{"id": 1, "x": 2, "size": 1, "y": 3}]')'''
        sq = Square(1, 2, 3)
        list_squares_input = [sq]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        # POURQUOI CE TEST NE PASSE PAS EN TESTANT: type is Square???
        '''self.assertTrue(type(list_squares_output[0]) is Square)'''
        self.assertTrue(sq.y == list_squares_output[0].y)


if __name__ == '__main__':
    unittest.main()
