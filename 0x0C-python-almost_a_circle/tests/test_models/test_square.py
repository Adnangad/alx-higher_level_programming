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
    def test_is_subclass(self):
        b = Square(5)
        self.assertIsInstance(b, Square)

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

    def test_size_setter(self):
        """Tests the setter."""
        b = Square(25)
        b.size = 22
        self.assertEqual(22, b.size)

    def test_update_args(self):
        """Tests the update method."""
        c = Square(11, 12, 13, 14)
        c.update(1, 2, 3, 4)
        cap = StringIO()
        sys.stdout = cap
        print(c)
        sys.stdout = sys.__stdout__
        rez = cap.getvalue().strip()
        d = "[Square] (1) 3/4 - 2"
        self.assertEqual(d, rez)

    def test_update_kwargs(self):
        """Tests the update method."""
        c = Square(11, 12, 13, 14)
        c.update(x=3)
        cap = StringIO()
        sys.stdout = cap
        print(c)
        sys.stdout = sys.__stdout__
        rez = cap.getvalue().strip()
        d = "[Square] (14) 3/13 - 11"
        self.assertEqual(d, rez)

    def test_to_dict(self):
        """Tests the to_dict method."""
        c = Square(2, 4, 6, 8)
        d = c.to_dictionary()
        f = {
                "id": 8, "x": 4, "size": 2, "y": 6
                }
        self.assertDictEqual(d, f)

    def test_to_dict_withother_methods(self):
        """Tests the dict method with other methods."""
        c = Square(2, 4, 6, 8)
        d = c.to_dictionary()
        e = Square(1, 3, 5, 9)
        e.update(**d)
        self.assertNotEqual(c, e)


if __name__ == '__main__':
    unittest.main()
