#!/usr/bin/python3
""" A rectangle Modules"""


class Rectangle:
    """Define A Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Intializing the rectangle
        Args:
            width: the rectangle width
            height the rectangle height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """retrive the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrive the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """return the rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        area_print = ""
        if self.width == 0 or self.height == 0:
            return area_print
        for i in range(self.height):
            area_print += str(self.print_symbol) * self.width
            if i != self.height - 1:
                area_print += "\n"
        return area_print

    def __repr__(self) -> str:
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
