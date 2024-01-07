#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_if_list_is_empty(self):
        rez = max_integer([])
        self.assertIsNone(None)

    def test_positive_num(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_negative_num(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_all_num(self):
        self.assertEqual(max_integer([-1, 2, -3]), 2)

    def test_error_val(self):
        self.assertRaises(TypeError, max_integer, [1, 2, 'a'])
        self.assertRaises(TypeError, max_integer, [1, 2, 2.5])
        self.assertRaises(TypeError, max_integer, [1, 2, 3.0, "Hello"])
