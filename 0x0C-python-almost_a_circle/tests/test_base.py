#!/usr/bin/python3
"""defines a unittest for base.py"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """reps test cases"""
    def testbase_id_increment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_custom_id(self):
        b = Base(100)
        self.assertEqual(b.id, 100)

    def testing_base_3(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id + 2, b3.id)

    def test_with_redeclaring(self):
        b = Base(10)
        b.id = 13
        self.assertEqual(b.id, 13)

    def testing_with_None(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id + 1, b2.id)

    def testing_after_unique_declaration(self):
        b1 = Base()
        b2 = Base(17)
        b3 = Base()
        self.assertEqual(b1.id + 1, b3.id)

    def test_string_id(self):
        self.assertEqual("three", Base("three").id)

    def test_with_dict(self):
        self.assertEqual({"b1": 3, "b2": 7}, Base({"b1": 3, "b2": 7}).id)

    def test_with_bool(self):
        self.assertEqual(True, Base(True).id)

    def test_with_2args(self):
        with self.assertRaises(TypeError):
            Base(2, 7)

if __name__ == "__main__":
    unittest.main()
