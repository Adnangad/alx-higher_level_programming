#!/usr/bin/python3
"""Defines a SizeError class."""


class SizeError(Exception):
    """Represents an empty SizeError."""
    pass


"""Defines a Square class."""


class Square:
    """Represents a square with a specific size."""
    def __init__(self, size=0):
        """Initializes the Square instance.
        Args:
            size (int): The size of the square.
        """
        self.__size = size
        if not isinstance(size, int):
            raise SizeError("size must be an integer")
        if size < 0:
            raise SizeError("size must be >= 0")

    @property
    def size(self):
        """Retrieves the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of size."""
        self.__size = value
        if not isinstance(value, int):
            raise SizeError("size must be an integer")
        if value < 0:
            raise SizeError("size must be >= 0")

    def area(self):
        """Return the area."""
        return self.__size * self.__size
