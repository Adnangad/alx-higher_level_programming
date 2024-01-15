#!/usr/bin/python3
"""
This module tests functions and classes.
"""
import unittest
import os
import json
from models.base import Base
from models.rectangle import Rectangle


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
        self.assertEqual(Base._Base__nb_objects, 2)

    def test_if_the_not_works(self):
        a = Base()
        self.assertEqual(Base._Base__nb_objects, a.id)

    def test_object_attribute(self):
        a = Base()
        self.assertTrue(hasattr(a, 'id'))

    def test_static_method(self):
        b = Rectangle(10, 20, 30, 40, 50)
        d = b.to_dictionary()
        c = Base.to_json_string([d])
        e = json.dumps([{"x": 30, "y": 40, "id": 50, "height": 20, "width": 10}])
        self.assertEqual(e, c)

if __name__ == '__main__':
    unittest.main()
