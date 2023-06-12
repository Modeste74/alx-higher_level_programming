#!/usr/bin/python3
"""define a class BaseGeometry"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """represents a rectangle"""
    def __init__(self, width, height):
        """intializes the rectangle"""
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
