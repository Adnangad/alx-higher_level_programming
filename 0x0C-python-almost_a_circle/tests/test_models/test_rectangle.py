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
        """
        Just a setup.
        """
        self.rectangle = Rectangle(20, 40)

    def test_init_of_width(self):
        """
        Tests the width att.
        """
        with self.assertRaises(TypeError):
            x = Rectangle("h", 20)

        with self.assertRaises(TypeError):
            x = Rectangle(20.5, 20)

    def test_init_of_height(self):
        """
        Tests the height att.
        """
        with self.assertRaises(TypeError):
            x = Rectangle(20, 20.5)

        with self.assertRaises(TypeError):
            x = Rectangle(20, "h")

    def test_init_of_x(self):
        """
        Tests the x att.
        """
        with self.assertRaises(TypeError):
            x = Rectangle(10, 20, "hello")

        with self.assertRaises(TypeError):
            x = Rectangle(20, 20, 20.5)

    def test_init_of_y(self):
        """
        Tests the y att.
        """
        with self.assertRaises(TypeError):
            x = Rectangle(10, 20, 30, 30.5)

        with self.assertRaises(TypeError):
            x = Rectangle(20, 20, 30, "Hello")

    def test_valueerror_forw_init(self):
        """
        Tests the width att for err.
        """
        with self.assertRaises(ValueError):
            s = Rectangle(0, 1)

        with self.assertRaises(ValueError):
            s = Rectangle(-1, 2)

    def test_valueerror_forh(self):
        """
        Tests the height att for err.
        """
        with self.assertRaises(ValueError):
            t = Rectangle(1, 0)

        with self.assertRaises(ValueError):
            t = Rectangle(2, -1)

    def test_valueerror_forx(self):
        """
        Tests the x att for err.
        """
        with self.assertRaises(ValueError):
            b = Rectangle(1, 2, 3, -1)

    def test_valueerror_fory(self):
        """
        Tests the y att for err.
        """
        with self.assertRaises(ValueError):
            b = Rectangle(1, 2, 3, -1)

    def test_typeerror_forw(self):
        """
        Tests the width input.
        """
        with self.assertRaises(TypeError):
            self.rectangle.width = 20.5

        with self.assertRaises(TypeError):
            self.rectangle.width = "hello"

    def test_typeerror_forh(self):
        """
        Tests the height input.
        """
        with self.assertRaises(TypeError):
            self.rectangle.height = 20.5

        with self.assertRaises(TypeError):
            self.rectangle.height = "hello"

    def test_typeerror_forx(self):
        """
        Tests the x input.
        """
        with self.assertRaises(TypeError):
            self.rectangle.x = 20.5

        with self.assertRaises(TypeError):
            self.rectangle.x = "hello"

    def test_typeerror_fory(self):
        """
        Tests the y input.
        """
        with self.assertRaises(TypeError):
            self.rectangle.y = 20.5

        with self.assertRaises(TypeError):
            self.rectangle.y = "hello"

    def test_valueerror_forw(self):
        """
        Tests the width input for valueerr.
        """
        with self.assertRaises(ValueError):
            self.rectangle.width = 0

        with self.assertRaises(ValueError):
            self.rectangle.width = -1

    def test_valueerror_forh(self):
        """
        Tests the height input for valueerr.
        """
        with self.assertRaises(ValueError):
            self.rectangle.height = 0

        with self.assertRaises(ValueError):
            self.rectangle.height = -1

    def test_valueerror_forx(self):
        """
        Tests the x input for valueerr.
        """
        with self.assertRaises(ValueError):
            self.rectangle.x = -1

    def test_valueerror_fory(self):
        """
        Tests the y input for valueerr.
        """
        with self.assertRaises(ValueError):
            self.rectangle.y = -1

    def test_are(self):
        """
        Tests the area method.
        """
        b = Rectangle(20, 3)
        self.assertEqual(60, b.area())

    def test_str(self):
        c = Rectangle(4, 6, 2, 1, 12)
        cap = StringIO()
        sys.stdout = cap
        print(c)
        sys.stdout = sys.__stdout__
        rez = cap.getvalue().strip()
        d = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(d, rez)

    def test_update_args(self):
        """Tests the update method."""
        c = Rectangle(1, 3, 9, 7, 11)
        c.update(22, 25)
        cap = StringIO()
        sys.stdout = cap
        print(c)
        sys.stdout = sys.__stdout__
        rez = cap.getvalue().strip()
        d = "[Rectangle] (22) 9/7 - 25/3"
        self.assertEqual(d, rez)

    def test_update_kwargs(self):
        """Tests the update method."""
        c = Rectangle(1, 3, 9, 7, 11)
        c.update(width=29, height=50)
        cap = StringIO()
        sys.stdout = cap
        print(c)
        sys.stdout = sys.__stdout__
        rez = cap.getvalue().strip()
        d = "[Rectangle] (11) 9/7 - 29/50"
        self.assertEqual(d, rez)

    def test_dict(self):
        """Tests the dict method."""
        c = Rectangle(1, 2, 3, 4, 5)
        d = c.to_dictionary()
        cap = StringIO()
        sys.stdout = cap
        print(d)
        sys.stdout = sys.__stdout__
        rez = cap.getvalue().strip()
        e = {
                'x': 3, 'y': 4, 'id': 5, 'height': 2, 'width': 1
                }
        req = str(e)
        self.assertEqual(req, rez)

    def test_dict_again(self):
        """Tests the dict method."""
        c = Rectangle(1, 2, 3, 4)
        d = c.to_dictionary()
        e = {
                'x': 3, 'y': 4, 'id': 9, 'height': 2, 'width': 1
                }
        self.assertEqual(e, d)


if __name__ == '__main__':
    unittest.main()
