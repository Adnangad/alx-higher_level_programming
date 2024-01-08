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
        if not isinstance(self.value, int):
            raise TypeError("<name> must be an integer")
        if self.value <= 0:
            raise ValueError("<name> must be greater than 0")
