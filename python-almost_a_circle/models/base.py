#!/usr/bin/python3
"""Write the first class Base"""
import json


class Base():
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns json string rep of list_dict"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """writes Json string to file"""
        if list_objs:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open(f"{cls.__name__}", "w") as f:
            f.write(cls.to_json_string(list_objs))