#!/usr/bin/python3
"""Definition of function my_list"""


class MyList(list):
    """Class Mylist with list in inherit"""

    def print_sorted(self):
        """"Function that prints the list, but sorted """
        for item in self:
            if not isinstance(item, int):
                raise TypeError("not all elements in list are integer")
        print(sorted(self))
