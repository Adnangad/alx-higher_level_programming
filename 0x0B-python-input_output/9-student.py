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

    def to_json(self):
        s = vars(self)
        rez = {}
        for a, b in s.items():
            if isinstance(b, (list, int, str, bool, dict)):
                rez[a] = b
        return rez
