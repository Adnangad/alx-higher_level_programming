#!/usr/bin/python3
"""
This module contains a class.
"""


class BaseGeometry:
    """
    This is func raises an exception.
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        if not isinstance(self.name, str):
            raise TypeError("{} must be a string".format(self.name))
        if not isinstance(self.value, int):
            raise TypeError("{} must be an integer".format(self.name))
        if self.value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
