#!/usr/bin/python3
"""
This module tests the Square class.
"""
import unittest
import re
import sys
from io import StringIO
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    The Tests Begin.
    """
    def test_init_of_attrsize(self):
        """This tests the size att."""
        b = Square(5)
        self.assertEqual(5, b.width)

    def test_atrr_x(self):
        """Tests x, y , id att."""
        b = Square(5, 10, 15, 20)
        self.assertEqual(10, b.x)
        self.assertEqual(15, b.y)
        self.assertEqual(20, b.id)

    def test_attr_errors(self):
        """Tests Errors."""
        with self.assertRaises(TypeError):
            b = Square("Hello")
            b = Square(6.6)
            b = Square(2, "Hello")
            b = Square(2, 2.5)
            b = Square(2, 4, "H")
            b = Square(2, 4, 4.5)
            b = Square(2, 4, 6, "H")

    def test_attr_value_errors(self):
        """Tests val errors."""
        with self.assertRaises(ValueError):
            b = Square(0)
            b = Square(-1)
            b = Square(10, -1)
            b = Square(10, 2, -1)

    def test_area(self):
        """Tests Area."""
        b = Square(20)
        self.assertEqual(400, b.area())


if __name__ == '__main__':
    unittest.main()
