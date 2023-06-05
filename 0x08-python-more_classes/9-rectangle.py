#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Representation of Rectangle
    with private attributes weight
    and height
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with
        sides width and height
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrives the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width
        to value given
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrive the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height to value
        given
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates the area
        of the rectangle
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """calculates the perimeter
        of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__height + self.__width)

    def __str__(self):
        """returns a string representation
        of an object
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        rectangle = str(self.print_symbol) * self.__width + "\n"
        rectangle *= self.__height
        return rectangle

    def __repr__(self):
        """ returns a string
        representation of an object
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """used to define the
        clean-up action or finalization
        logic for an object
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """return biggest rectangle
        based of the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """used to create a
        square within the class
        rectangle
        """
        return cls(size, size)
