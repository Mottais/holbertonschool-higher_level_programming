#!/usr/bin/python3
import unittest
import os
import json
import sys
from models.rectangle import Base
from models.rectangle import Rectangle
from io import StringIO
"""Runs test cases for the Rectangle module"""


class test_rectangle(unittest.TestCase):
    """Testing rectangle"""

    def test_arectangle_id(self):
        """Test the id for Rectangle"""
        rect = Rectangle(1, 3, 0, 0, 199)
        self.assertEqual(199, rect.id)

    def test_width_string(self):
        """Testing for other than int"""
        with self.assertRaises(TypeError):
            rect = Rectangle("1", 5)

    def test_width_negative(self):
        """Testing with negative int"""
        with self.assertRaises(ValueError):
            rect = Rectangle(-4, 5)

    def test_str_overload(self):
        r = Rectangle(5, 10, 8, 7, 88)
        self.assertEqual(r.__str__(), "[Rectangle] (88) 8/7 - 5/10")

    def test_to_dict(self):
        """Testing the type that is returned from the to_dictionary method"""
        r1 = Rectangle(5, 4)
        self.assertEqual(type(r1.to_dictionary()), dict)

    def test_to_dict_print(self):
        """Testing the dict that will be printed"""
        r1 = Rectangle(5, 4, 0, 0, 400)
        r1_dict = r1.to_dictionary()
        self.assertEqual(r1_dict,
        {"width": 5, "height": 4, "x": 0, "y": 0, "id": 400})

    def test_missing_height(self):
        """Expecting a type error because height and width are missing"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_missing_width(self):
        """Expecting an error because width is missing"""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_str_representation(self):
        """ Testing string rep """
        rect = Rectangle(5, 4, 1, 2, 42)
        expected_str = "[Rectangle] (42) 1/2 - 5/4"
        self.assertEqual(str(rect), expected_str)

    def test_saving_to_file(self):
        """Testing saving a file into json format"""
        try:
            os.remove("Rectangle.json")
        except:
            pass
        r1 = Rectangle(5, 10, 0, 0, 346)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as file:
            content = file.read()
        t = [{"width": 5, "height": 10, "x": 0, "y": 0, "id": 346}]
        self.assertEqual(t, json.loads(content))

    def test_saving_to_file_None(self):
        """Testing saving a file into json format sending None"""
        try:
            os.remove("Rectangle.json")
        except:
            pass
        r1 = Rectangle(5, 10, 0, 0, 346)
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            content = file.read()
        self.assertEqual("[]", content)

    def test_saving_to_file_type(self):
        """Testing saving a file into json format sending None"""
        try:
            os.remove("Rectangle.json")
        except:
            pass
        r1 = Rectangle(5, 10, 0, 0, 346)
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            content = file.read()
        self.assertEqual(str, type(content))
        try:
            os.remove("Rectangle.json")
        except:
            pass

    def test_json_string_type(self):
        """Testing the returned type"""
        list_input = [
            {"id": 2089, "width": 10, "height": 4},
            {"id": 2712, "width": 1, "height": 7},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)

    def test_json_string(self):
        """Testing that the json string gets converted into a list"""
        list_input = [
            {"id": 2089, "width": 10, "height": 4},
            {"id": 2712, "width": 1, "height": 7},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        s1 = {"id": 2089, "width": 10, "height": 4}
        s2 = {"height": 7, "id": 2712, "width": 1}
        self.assertEqual(list_output[0], s1)
        self.assertEqual(list_output[1], s2)

    def test_dict_to_instance(self):
        """test that an instance is created from a dict"""
        r1 = Rectangle(5, 8, 3)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_isnot_dict_to_instance(self):
        """test that an instance is created from a dict"""
        r1 = Rectangle(109, 80, 76)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_load_from_file_not_the_same(self):
        """Checking that an object was created from the
        list but has a different adress."""
        r1 = Rectangle(10, 7, 2, 8)
        list_rectangles_input = [r1]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertNotEqual(id(r1), id(list_rectangles_output[0]))

    def test_load_from_file_same_width(self):
        """Checking that an object was created from the
        list and has the same witdh"""
        r1 = Rectangle(10, 7, 2, 8)
        list_rectangles_input = [r1]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(r1.width, list_rectangles_output[0].width)

    def test_load_from_file_same_height(self):
        """Checking that an object was created from the
        list and has the same height"""
        r1 = Rectangle(10, 7, 2, 8)
        list_rectangles_input = [r1]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(r1.height, list_rectangles_output[0].height)

    def test_load_from_file_same_x(self):
        """Checking that an object was created from the
        list and has the same x"""
        r1 = Rectangle(10, 7, 2, 8)
        list_rectangles_input = [r1]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(r1.x, list_rectangles_output[0].x)

    def test_load_from_file_same_y(self):
        """Checking that an object was created from the
        list and has the same y"""
        r1 = Rectangle(10, 7, 2, 8)
        list_rectangles_input = [r1]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(r1.y, list_rectangles_output[0].y)

    def test_display_square(self):
        """Checking the stdout output by capturing it"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(10, 4)
        r1.display()
        sys.stdout = sys.__stdout__
        output = "##########\n" + "##########\n" + "##########\n" + "##########\n"
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_display_square_size_one(self):
        """Checking the stdout output by capturing it"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(1, 2)
        r1.display()
        sys.stdout = sys.__stdout__

        output = "#\n#\n"
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_display_square_size_zero(self):
        """Checking the stdout output by capturing it"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(3, 7)
        r1.display()
        sys.stdout = sys.__stdout__
        output = "###\n###\n###\n###\n###\n###\n###\n"
        self.assertEqual(capturedOutput.getvalue(), output)

    if __name__ == '__main__':
        unittest.main()
