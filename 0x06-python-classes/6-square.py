#!/usr/bin/python3
"""Define a class Sqaure """
class Square:
    """Represents a square with
    attribute size
    """
    def __init__(self, size=0, position=(0, 0)):
        """initializes the square with 
        args size of type int and position
        """
        self.__size = size
        self.__position = position
    @property
    def size(self):
        """Retrives the size """
        return self.__size
    @size.setter
    def size(self, value):
        """sets size to value """
        if not isinstance(value, int):
            """checks is size is of int type """
            raise TypeError("size must be an integer")
        elif value < 0:
            """size must be above 0 """
            raise ValueError("size must be >= 0")
        else:
            """sets size to value """
            self.__size = value
    @property
    def position(self):
        """retrives the position """
        return self.__position
    def position(self, value):
        """sets the positon of the square """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(num, int) for num in value) or any(num < 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__postion = value
    def area(self):
        """calculates area of square
         using the attribute size
        """
        return self.__size ** 2
    def my_print(self):
        """Prints out the square using '#' """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " *self.__position[0] + '#' * self.__size)
