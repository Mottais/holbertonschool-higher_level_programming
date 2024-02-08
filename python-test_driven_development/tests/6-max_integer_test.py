#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxIntegerWithIntegers(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([0, -1, -2, -3]), 0)
        self.assertEqual(max_integer([1, 0, -1, -2]), 1)
        self.assertEqual(max_integer([1]*1000), 1)
        self.assertEqual(max_integer(list(range(1000))), 999)
        self.assertEqual(max_integer([1, 2, 3.5, 4]), 4)
        self.assertEqual(max_integer([1, 2, 3, 4]*1000), 4)
        self.assertEqual(max_integer([1, 2, 3, 4, 5]*0), None)
        self.assertEqual(max_integer([1, 2, 3, 4, 5]*-1), None)
        self.assertEqual(max_integer([1, 2, 3, 4, float('inf')]), float('inf'))
        self.assertEqual(max_integer([1, 2, 3, 4, float('-inf')]), 4)


class TestMaxIntegerWithStrings(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')
        self.assertEqual(max_integer(['abc', 'bcd', 'cde']), 'cde')


class TestMaxIntegerWithTuples(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([(1, 2), (3, 4), (5, 6)]), (5, 6))


class TestMaxIntegerWithNonComparableValues(unittest.TestCase):
    def test_max_integer(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, "3", 4])
        with self.assertRaises(TypeError):
            max_integer([1, 2, [3], 4])
        with self.assertRaises(TypeError):
            max_integer([1, 2, None, 4])
        with self.assertRaises(TypeError):
            max_integer([1, 2, (3, 4), 5])


if __name__ == '__main__':
    unittest.main()
