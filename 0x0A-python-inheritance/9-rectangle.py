#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle"""

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""

        return self.__width * self.__height

    def __str__(self):
        """Return representation of a Rectangle."""

        st = "[" + str(self.__class__.__name__) + "] "
        st += str(self.__width) + "/" + str(self.__height)
        return st
