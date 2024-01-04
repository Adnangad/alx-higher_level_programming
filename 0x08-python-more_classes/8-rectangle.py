#!/usr/bin/python3
"""
This module creates a class.
"""


class Rectangle:
    """
    Initializes the class.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Sets the var."""
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

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
            x += str(self.print_symbol) * self.width + "\n"
        return x[:-1]

    def __repr__(self):
        """Return String rep."""
        if self.width == 0 or self.height == 0:
            return ""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
