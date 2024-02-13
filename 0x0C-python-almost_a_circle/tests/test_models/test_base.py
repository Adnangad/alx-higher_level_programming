#!/usr/bin/python3
"""
This module tests functions and classes.
"""
import unittest
import os
from models.base import Base


class TestBase(unittest.TestCase):
    """
    This class tests Base class.
    """
    def test_id_value(self):
        b = Base(10)
        self.assertIsInstance(b, Base)
        self.assertEqual(b.id, 10)

    def test_class_atrribute(self):
        c = Base()
        d = Base()
        self.assertEqual(Base.__nb_objects, 2)

    def test_if_the_not_works(self):
        a = Base()
        self.assertEqual(Base.__nb_objects, a.id)

    def test_object_attribute(self):
        a = Base()
        self.assertTrue(hasattr(a, id))

if __name__ == '__main__':
    unittest.main()
