#!/usr/bin/python3
"""
This module tests the rectangle class.
"""
import unittest
import sys
from io import StringIO
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(20, 40)

    def test_init_of_width(self):
        with self.assertRaises(TypeError):
            x = Rectangle("h", 20)

        with self.assertRaises(TypeError):
            x = Rectangle(20.5, 20)

    def test_init_of_height(self):
        with self.assertRaises(TypeError):
            x = Rectangle(20, 20.5)

        with self.assertRaises(TypeError):
            x = Rectangle(20, "h")

    def test_init_of_x(self):
        with self.assertRaises(TypeError):
            x = Rectangle(10, 20, "hello")

        with self.assertRaises(TypeError):
            x = Rectangle(20, 20, 20.5)

    def test_init_of_y(self):
        with self.assertRaises(TypeError):
            x = Rectangle(10, 20, 30, 30.5)

        with self.assertRaises(TypeError):
            x = Rectangle(20, 20, 30, "Hello")

    def test_valueerror_forw_init(self):
        with self.assertRaises(ValueError):
            s = Rectangle(0, 1)

        with self.assertRaises(ValueError):
            s = Rectangle(-1, 2)

    def test_valueerror_forh(self):
        with self.assertRaises(ValueError):
            t = Rectangle(1, 0)

        with self.assertRaises(ValueError):
            t = Rectangle(2, -1)

    def test_valueerror_forx(self):
        with self.assertRaises(ValueError):
            b = Rectangle(1, 2, 3, -1)

    def test_valueerror_fory(self):
        with self.assertRaises(ValueError):
            b = Rectangle(1, 2, 3, -1)

    def test_typeerror_forw(self):
        with self.assertRaises(TypeError):
            self.rectangle.width = 20.5

        with self.assertRaises(TypeError):
            self.rectangle.width = "hello"

    def test_typeerror_forh(self):
        with self.assertRaises(TypeError):
            self.rectangle.height = 20.5

        with self.assertRaises(TypeError):
            self.rectangle.height = "hello"

    def test_typeerror_forx(self):
        with self.assertRaises(TypeError):
            self.rectangle.x = 20.5

        with self.assertRaises(TypeError):
            self.rectangle.x = "hello"

    def test_typeerror_fory(self):
        with self.assertRaises(TypeError):
            self.rectangle.y = 20.5

        with self.assertRaises(TypeError):
            self.rectangle.y = "hello"

    def test_valueerror_forw(self):
        with self.assertRaises(ValueError):
            self.rectangle.width = 0

        with self.assertRaises(ValueError):
            self.rectangle.width = -1

    def test_valueerror_forh(self):
        with self.assertRaises(ValueError):
            self.rectangle.height = 0

        with self.assertRaises(ValueError):
            self.rectangle.height = -1

    def test_valueerror_forx(self):
        with self.assertRaises(ValueError):
            self.rectangle.x = -1

    def test_valueerror_fory(self):
        with self.assertRaises(ValueError):
            self.rectangle.y = -1

    def test_are(self):
        b = Rectangle(20, 3)
        self.assertEqual(60, b.area())

    def test_disp(self):
        cap = StringIO()
        sys.stdout = cap
        b = Rectangle(2, 1)
        b.display()
        sys.stdout = sys.__stdout__
        rez = cap.getvalue().strip()
        c = "##"
        self.assertEqual(c, rez)

    def test_str(self):
        c = Rectangle(4, 6, 2, 1, 12)
        cap = StringIO()
        sys.stdout = cap
        print(c)
        sys.stdout = sys.__stdout__
        rez = cap.getvalue().strip()
        d = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(d, rez)


if __name__ == '__main__':
    unittest.main()
