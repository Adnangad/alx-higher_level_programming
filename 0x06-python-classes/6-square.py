#!/usr/bin/python3
"""Defines a SizeError class."""


class SizeError(Exception):
    """Represents an empty SizeError."""
    pass

"""Defines a PositionError class."""


class PositionError(Exception):
    """Represents an empty SizeError."""
    pass

"""Defines a Square class."""


class Square:
    """Represents a square with a specific size."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the Square instance.
        Args:
            size (int): The size of the square.
            position(int): The tuples.
        """
        self.__size = size
        self.__position = position
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

    @property
    def position(self):
        """Retreives the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position values."""
        if (
                not isinstance(value, tuple)
                or len(value) != 2
                or not all(isinstance(num, int) for num in value)
                or not all(num >= 0 for num in value)
            ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area."""
        return self.__size * self.__size

    def my_print(self):
        """Prints the area."""
        if self.__size == 0:
            print()
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
