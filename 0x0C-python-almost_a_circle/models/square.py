#!/usr/bin/python3
"""
This module contains a subclass.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class inherits metods and att from Rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Sets the attributes.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returns the size."""
        return self.width

    @size.setter
    def size(self, val):
        """Sets the size."""
        self.width = val
        self.height = val

    def __str__(self):
        """
        Prints the info.
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """
        Sets the values.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key , val in kwargs.items():
                if key == "id":
                    if val is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = val
                elif key == "size":
                    self.size = val
                elif key == "x":
                    self.x = val
                elif key == "y":
                    self.y = val

    def to_dictionary(self):
        """Returns a dict containing values."""
        return {
                "id": self.id,
                "x": self.x,
                "size": self.size,
                "y": self.y
                }
