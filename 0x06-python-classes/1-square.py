#!/usr/bin/python3
"""Define a class Square"""
class Square:
    """Representation of a square
    with private attribute size"""
    def __init__(self, size):
        """Initialize the square with the
        args: size which is the size ofthe square
        """
        self.__size = size
