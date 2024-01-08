#!/usr/bin/python3
"""
This module contains a subclass.
"""


"""
importing.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """
    This class inhertis from class BaseGeometry.
    """
    def __init__(self, width, height):
        b = BaseGeometry()
        b.integer_validator("width", width)
        b.integer_validator("height", height)
        self.__width = width
        self.__height = height
