#!/usr/bin/python3
"""define a unittest for the base.py"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def tearDown(self):
        """Delete any created files"""
        file_extensions = ["json", "csv"]
        for cls in [Rectangle, Square, Base]:
            for ext in file_extensions:
                filename = f"{cls.__name__}.{ext}"
                try:
                    os.remove(filename)
                except FileNotFoundError:
                    pass

    def test_base_instantiation(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_base_to_json_string(self):
        r = Rectangle(10, 7, 2, 8, 6)
        json_str = Base.to_json_string([r.to_dictionary()])
        self.assertEqual(str, type(json_str))

    def test_base_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.isfile("Rectangle.json"))

    def test_base_from_json_string(self):
        json_str = '[{"id": 89, "width": 10, "height": 4}]'
        objs = Base.from_json_string(json_str)
        self.assertEqual(list, type(objs))

    def test_base_create(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(r1, r2)

    def test_base_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        objs = Rectangle.load_from_file()
        self.assertEqual(list, type(objs))

    def test_base_save_to_file_csv(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([r])
        self.assertTrue(os.path.isfile("Rectangle.csv"))

    def test_base_load_from_file_csv(self):
        r = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file_csv([r])
        objs = Rectangle.load_from_file_csv()
        self.assertEqual(list, type(objs))


if __name__ == "__main__":
    unittest.main()
