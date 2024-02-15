#!/usr/bin/python3
"""this file contain the class student"""


class Student:
    """class of student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return the choosen attributes or all if attrs=None"""
        if attrs is None:
            return self.__dict__
        Dict_Attrs_values = {}
        for Attribut in attrs:
            if Attribut in self.__dict__:
                Dict_Attrs_values[Attribut] = self.__dict__[Attribut]
        return Dict_Attrs_values

    def reload_from_json(self, json):
        """load json to replace value of attribut of this object"""
        for key, value in json.items():
            self.__dict__[key] = value
