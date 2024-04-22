#!/usr/bin/python3
"""Defines unittests for models/square.py."""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_instantiation(self):
        s = Square(10)
        self.assertIsInstance(s, Square)

    def test_size(self):
        s = Square(10)
        self.assertEqual(s.size, 10)
        s.size = 5
        self.assertEqual(s.size, 5)

    def test_position(self):
        s = Square(10, 2, 3)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        s.x = 5
        s.y = 7
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 7)

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_str_representation(self):
        s = Square(4, 1, 2, 1)
        self.assertEqual(str(s), "[Square] (1) 1/2 - 4")

    def test_update(self):
        s = Square(10, 2, 3, 1)
        s.update(5, 4, 5, 2)
        self.assertEqual(s.size, 4)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 2)

    def test_to_dictionary(self):
        s = Square(10, 2, 3, 1)
        d = s.to_dictionary()
        self.assertEqual(d, {"id": 1, "size": 10, "x": 2, "y": 3})


if __name__ == "__main__":
    unittest.main()
