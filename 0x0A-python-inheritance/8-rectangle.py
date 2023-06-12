#!/usr/bin/python3
"""define a class Rectangle that
inherits the attributes of
BaseGeometry
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Reps a rectangle"""
    def __init__(self, width, height):
        """intializes the rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
