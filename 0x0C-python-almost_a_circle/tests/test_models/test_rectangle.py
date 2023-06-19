#!/usr/bin/python3
"""defines some unittest"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_rect_instance(unittest.TestCase):
    def test_isinstance_base(self):
        self.assertIsInstance(Rectangle(8, 3), Base)

    def test_isinstance_rect(self):
        self.assertIsInstance(Rectangle(8, 3), Rectangle)

    def test_with_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_nb_instance_in_rect(self):
        r1 = Rectangle(8, 3)
        r2 = Rectangle(7, 5)
        self.assertEqual(r1.id + 1, r2.id)

    def test_with_one_args(self):
        with self.assertRaises(TypeError):
            Rectangle(8)

    def test_to_locate_id(self):
        r2 = Rectangle(12, 7, 9, 2, 5)
        self.assertEqual(5, r2.id)

    def test_with_too_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle(12, 7, 9, 2, 5, 8)

    def with_priv_attributes(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(15, 4).__width)

    def attribute_call(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 4, 5, 6, 9).__y)

    def test_width_getter(self):
        self.assertEqual(10, Rectangle(10, 4, 5, 6, 9).width)

    def test_width_setter(self):
        r1 = Rectangle(10, 4, 5, 6, 9)
        r1.width = 7
        self.assertEqual(7, r1.width)

    def test_height_getter(self):
        self.assertEqual(4, Rectangle(10, 4, 5, 6, 9).height)

    def test_height_setter(self):
        r = Rectangle(10, 4, 5, 6, 9)
        r.height = 3
        self.assertEqual(3, r.height)

    def x_getter(self):
        self.assertEqual(5, Rectangle(10, 4, 5, 6, 9).x)

    def x_setter(self):
        r = Rectangle(10, 4, 5, 6, 9)
        r.x = 4
        self.assertEqual(4, r.x)

    def y_getter(self):
        self.assertEqual(6, Rectangle(10, 4, 5, 6, 9).y)

    def y_setter(self):
        r = Rectangle(10, 4, 5, 6, 9)
        r.y = 7
        self.assertEqual(7, r.y)


class validity_check(unittest.TestCase):
    """unittest for checking for the validations of args passed"""
    def string_width_passed(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("ten", 4, 5, 6, 9)

    def none_passed(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 4, 5, 6, 9)

    def float_passed(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, 4.25, 5, 6, 9)

    def complex_passed(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, complex(7), 5, 6, 9)

    def boolean_passed(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, True, 5, 6, 9)

    def negative_values_passed(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 4, -5, 6, 9)

    def zero_passed_in_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(10, 0, 5, 6, 9)

    def nan_passed(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, float('nan'), 7, 6, 9)


class operations_check(unittest.TestCase):
    """unittest for checking if operations are working"""
    def test_area_normal_values(self):
        r = Rectangle(15, 2, 5, 6, 9)
        self.assertEqual(30, r.area())

    def test_with_large_nums(self):
        r = Rectangle(15484848484847447488393848, 2483737473829939283, 5, 6, 9)
        self.assertEqual(38460298458394362064201459793163845030730984, r.area())

    def area_with_updated_values(self):
        r = Rectangle(15, 2, 5, 6, 9)
        r.width = 45
        r.height = 32
        self.assertEqual(1440, r.area())

    def putting_an_args_when_area_called(self):
        with self.assertRaises(TypeError):
            r.area(2)

if __name__ == "__main__":
    unittest.main()
