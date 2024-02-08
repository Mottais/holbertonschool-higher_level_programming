#!/usr/bin/python3
import unittest

max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):

    def test_sorted_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_reverse_integer(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_string(self):
        self.assertEqual(max_integer("Hello"), "o")

    def test_only_one(self):
        self.assertEqual(max_integer([5]), 5)

    def test_negatif(self):
        self.assertEqual(max_integer([-5]), -5)

    def test_empty(self):
        self.assertEqual(max_integer(), None)

    def test_max_integer(self):
        self.assertEqual(max_integer([[1, 2, 3], [6, 7, 8]]), [6, 7, 8])

    def test_same(self):
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_mid(self):
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)
