#!/usr/bin/python3
"""
This module contains a class.
"""


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
