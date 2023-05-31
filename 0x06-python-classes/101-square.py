#!/usr/bin/python3
"""Define a square"""


class Square:
    """represents a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializez a square"""
        self._size = 0
        self._position = (0, 0)
        self.size = size
        self.position = position

    @property
    def size(self):
        """retrieves the size"""
        return self._size

    @size.setter
    def size(self, value):
        """sets the size to value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """retrives the position of square"""
        return self._postion

    @position.setter
    def position(self, value):
        """sets the position of the square"""
        if not isinstance(value, tuple) or len(value) != 2 or \
            not all(isinstance(val, int) and val >= 0 for val in value):
                raise TypeError("position must be a tuple of 2 positive integers")
        self._postion = value

    def area(self):
        """calculates area of the square"""
        return self._size ** 2

    def my_print(self):
        """print the square with '#'"""
        if self._size == 0:
            print()
            return
        for i in range(self._postion[1]):
            print()
        for i in range(self._size):
            print(" " * self._postion[0] * + "#" * self._size)

    def __str__(self):
        """return the square with '#'"""
        square_str = ""
        if self._size == 0:
            return square_str
        for i in range(self._position[1]):
            square_str += '\n'
        for i in range(self._size):
            for n in range(self._position[0]):
                square_str += " "
            for n in range(self._size):
                square_str += "#"
            square_str += "\n"
        return square_str
