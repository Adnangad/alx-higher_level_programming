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
