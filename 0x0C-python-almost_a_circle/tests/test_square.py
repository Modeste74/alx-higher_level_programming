#!/usr/bin/python3
"""defines some unittest"""
import unittest
from models.base import Base
from models.square import Square


class Test_rect_instance(unittest.TestCase):
    def test_isinstance_base(self):
        self.assertIsInstance(Square(8), Base)

    def test_isinstance_rect(self):
        self.assertIsInstance(Square(8), Square)

    def test_with_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_nb_instance_in_rect(self):
        s1 = Square(8, 5)
        s2 = Square(7, 3)
        self.assertEqual(s1.id + 1, s2.id)

    def test_with_one_args(self):
        self.assertEqual(8, Square(8).size)

    def test_to_locate_id(self):
        s2 = Square(12, 9, 2, 5)
        self.assertEqual(5, s2.id)

    def test_with_too_many_args(self):
        with self.assertRaises(TypeError):
            Square(2, 3, 4, 5, 6)

    def with_priv_attributes(self):
        with self.assertRaises(AttributeError):
            print(Square(15, 4).__size)

    def attribute_call(self):
        with self.assertRaises(AttributeError):
            print(Square(10, 4, 5, 6).__y)

    def test_size_getter(self):
        self.assertEqual(10, Square(10, 4, 5, 6).size)

    def test_size_setter(self):
        s1 = Square(10, 4, 5, 6)
        s1.size = 7
        self.assertEqual(7, s1.size)

    def x_getter(self):
        self.assertEqual(4, Square(10, 4, 5, 6).x)

    def x_setter(self):
        r = Square(10, 4, 5, 6)
        r.x = 9
        self.assertEqual(9, r.x)

    def y_getter(self):
        self.assertEqual(6, Square(10, 4, 5, 6).y)

    def y_setter(self):
        r = Square(10, 4, 5, 6)
        r.y = 7
        self.assertEqual(7, r.y)


class validity_check(unittest.TestCase):
    """unittest for checking for the validations of args passed"""
    def string_width_passed(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("ten", 4, 5, 6)

    def none_passed(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None, 4, 5, 6)

    def float_passed(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, 4.25, 5, 6)

    def complex_passed(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, complex(7), 5, 6)

    def boolean_passed(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 4, True, 6)

    def negative_values_passed(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(10, 4, -5, 6)

    def zero_passed_in_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 0, 5, 6)

    def nan_passed(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, float('nan'), 7, 6)


class operations_check(unittest.TestCase):
    """unittest for checking if operations are working"""
    def test_area_normal_values(self):
        s = Square(15, 2, 5, 6)
        self.assertEqual(225, s.area())

    def test_with_large_nums(self):
        s = Square(15484848484847447488393848, 5, 6, 9)
        self.assertEqual(239780532598682290168568336841037905140662764247104, s.area())

    def area_with_updated_values(self):
        s = Square(15, 2, 5, 6)
        s.size = 45
        self.assertEqual(2025, s.area())

    def putting_an_args_when_area_called(self):
        with self.assertRaises(TypeError):
            s.area(2)

if __name__ == "__main__":
    unittest.main()
