#!/usr/bin/python3
"""
This module contains a class.
"""
import json


class Base:
    """
    This class is the parent classs.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        This initializes the class for args.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts list_dict to json str format."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            b = json.dumps(list_dictionaries)
            return b

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the json str to a file."""
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                dc = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(dc))
