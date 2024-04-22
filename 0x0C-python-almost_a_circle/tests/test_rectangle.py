#!/usr/bin/python3
"""Defines unittests for rectangle.py"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.r = Rectangle(10, 2, 1, 1, 1)

    def test_instantiation(self):
        self.assertIsInstance(self.r, Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    # ... rest of the test methods ...


if __name__ == "__main__":
    unittest.main()
