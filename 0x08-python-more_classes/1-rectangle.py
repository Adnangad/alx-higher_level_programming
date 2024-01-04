#!/usr/bin/python3
"""
This module creates a class.
"""


class Rectangle:
    """
    Initializes the class.
    """

    def __init__(self, width=0, height=0):
        """Sets the var."""
        self.__width = width
        self.__height = height
    @property
    def width(self):
        """Gets the width."""
        return self.__width
    @width.setter
    def width(self, value):
        """Sets the width."""
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
    @property
    def height(self):
        """Gets the height."""
        return self.__height
    @height.setter
    def height(self, value):
        """Sets height."""
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
