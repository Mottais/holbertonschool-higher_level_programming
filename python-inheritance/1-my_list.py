#!/usr/bin/python3
"""class using the other class list as a model"""


class MyList(list):
    """addind function to print the sorted list"""
    def print_sorted(self):
        print(sorted(self))
