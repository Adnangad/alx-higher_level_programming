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

    def __str__(self):
        """
        Prints the info.
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
