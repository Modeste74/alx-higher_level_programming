#!/usr/bin/python3
"""Define a class Square"""

class Square:
    """Representation of a square
    with private attribute size 
    """

    def __init__(self, size):
        """Initialize the square with the

        Args:
            size(int): which is the size ofthe square

        Return:
            None

        """
        self.__size = size
