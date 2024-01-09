#!/usr/bin/python3
"""
This module contains a class.
"""


class Student:
    """
    The first func initializes arg.

    Args:
    first_name:the first name
    last_name:students last name
    age:students age

    Return:
    None.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
