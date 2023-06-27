#!/usr/bin/python3
""" A Module That Define A Square"""


class Square:
    """A Class That Represents A Square"""

    def __init__(self, size=0):
        """Intializing The Class Square
        Args:
            size: The size Of The Square
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate Area Of The Square
        Return: The Current Square Area"""
        return self.__size**2

    def __eq__(self, other):
        if isinstance(other, Square):
            return self.size == other.size
        return False

    def __lt__(self, other):
        if isinstance(other, Square):
            return self.size < other.size

    def __gt__(self, other):
        if isinstance(other, Square):
            return self.size > other.size

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)
