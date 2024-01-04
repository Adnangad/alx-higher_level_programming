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
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Gets the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area."""
        return self.width * self.height

    def perimeter(self):
        """Returns perimeter."""
        if self.width == 0 or self.height == 0:
            return 0
        return self.width + self.width + self.height + self.height

    def __str__(self):
        x = ""
        if self.width == 0 or self.height == 0:
            return x
        for i in range(self.height):
            for j in range(self.width):
                x += "#"
            x += "\n"
        return x

    def __repr__(self):
        if self.width == 0 or self.height == 0:
            return ""
        return f"Rectangle({self.width}, {self.height})"
