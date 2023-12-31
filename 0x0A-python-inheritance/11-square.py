#!/usr/bin/python3
"""
This module contains a subclass.
"""


"""
importing.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class inhertis from class BaseGeometry.
    """
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))
