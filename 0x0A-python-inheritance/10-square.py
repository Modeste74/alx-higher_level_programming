#!/usr/bin/python3
"""define a class BaseGeometry"""


class BaseGeometry:
    """intializes the class"""
    def area(self):
        """raises Exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """reps a rectangle"""
    def __init__(self, width, height):
        """initialzes the rectangle"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """returns the area
        of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """return a certain description"""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """represents a square"""
    def __init__(self, size):
        """uses the attributes in Rectangle"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns area of square"""
        return self.__size ** 2
