#!/usr/bin/python3
"""
Contient la classe 'Base'



"""
import json


class Base():
    """
    Class : Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize Identifiant
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries is []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of the JSON string representation json_string
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Converting a dict into a json string"""
        if list_objs:
            j = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        else:
            j = '[]'
        with open(cls.__name__ + '.json', 'w') as f:
            f.write(j)

    @classmethod
    def create(cls, **dictionary):
        """
        Return an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        if cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)

        return new
        '''
        ou bien
        for key, value in dictionary.items():
            if key == "width":
                width = value
            if key == "height":
                height = value
            if key == "x":
                x = value
            if key == "y":
                y = value
            if key == "size":
                size = value

        if cls.__name__ == "Rectangle":
            return cls(width, height, x, y)
        if cls.__name__ == "Square":
            return cls(size, x, y)
        '''

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances
        """
        try:
            with open(cls.__name__ + ".json", "r") as file:
                list_objs = cls.from_json_string(file.read())
        except FileNotFoundError:
            list_objs = []

        new_list_objs = []

        for obj in list_objs:
            new_list_objs.append(cls.create(**obj))

        return new_list_objs
