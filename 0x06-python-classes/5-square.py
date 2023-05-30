#!/usr/bin/python3
"""Define a class Sqaure """
class Square:
    """Represents a square with
    attribute size
    """
    def __init__(self, size=0):
        """initializes the square with 
        args size of type int
        """
        self.__size = size
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
            for i in range(self.__size):
                print("#" * self.__size)
