#!/usr/bin/python3
"""Define a class Sqaure"""


class Square:
    """Represents a square with
    attribute size
    """
    def __init__(self, size=0):
        """initializes the square with
        args size of type int
        """
        if not isinstance(size, int):
            """checks is size is of int type"""
            raise TypeError("size must be an integer")
        elif size < 0:
            """size must be above 0"""
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
