#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Will be used for
    unittest conducted on the module
    imported above
    """
    def tested_in_good_order(self):
        """Test a list in good order"""
        good_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(good_list), 4)

    def test_in_no_order(self):
        """Test in no order"""
        no_order = [1, 4, 3, 2]
        self.assertEqual(max_integer(no_order), 4)

    def test_one_int(self):
        """Testing one number list"""
        one_no = [9]
        self.assertEqual(max_integer(one_no), 9)

    def test_empty_list(self):
        """Tests an empty list"""
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_with_negative(self):
        """Testing with a negative number
        in the list
        """
        list_with_negative = [1, -4, 3, 2]
        self.assertEqual(max_integer(list_with_negative), 3)

    def test_with_floats(self):
        """Testing with floats"""
        float_list = [7.68, 5.75, 4.95, 9.75]
        self.assertEqual(max_integer(float_list), 9.75)

    def test_with_string(self):
        """Testing the string"""
        string_tst = "Modeste"
        self.assertEqual(max_integer(string_tst), 't')

    def test_when_nothing_is_passed(self):
        """Testing when nothing
        is passed
        """
        self.assertEqual(max_integer(""), None)

    def test_with_string_list(self):
        """Testing with list of strings"""
        string_list = ["Julia", "Sandoval", "Fernando"]
        self.assertEqual(max_integer(string_list), "Sandoval")


if __name__ == "__main__":
    unittest.main()
