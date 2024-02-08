#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest


max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_1_max_liste_int(self):
        self.assertTrue(max_integer([1, 2]) == 2)
        self.assertTrue(max_integer([-5, -700]) == -5)
        self.assertTrue(max_integer([77]) == 77)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertTrue(max_integer([1, 2, float('inf')]) == float('inf'))

    def test_2_max_liste_int_float(self):
        self.assertTrue(max_integer((8.2, 8.22, 1)) == 8.22)

    def test_3_Liste_of_strings(self):
        self.assertTrue(max_integer(["b", "a", "ba", "aaa"]) == "ba")

    def test_4_max_liste_of_tuple(self):
        self.assertTrue(max_integer([(1, 3), (1, 2, 1)]) == (1, 3))


class TestMaxInteger_TypeError(unittest.TestCase):
    def test_5_max_liste_TypeError(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, "3", 4])
        with self.assertRaises(TypeError):
            print(max_integer([1, 3], (1, 2, 1)))
        with self.assertRaises(TypeError):
            print(max_integer({8, 2, 1}))


class TestMaxInteger_ZeroDivisionError(unittest.TestCase):
    def test_6_max_liste_ZeroDivisionError(self):
        with self.assertRaises(ZeroDivisionError):
            max_integer([1, 2, 3, 4/0])


class TestMaxInteger_ValueError(unittest.TestCase):
    def test_7_max_liste_ValueError(self):
        with self.assertRaises(ValueError):
            max_integer([1, 2, 3, int("9" * 4301)])

