#!/usr/bin/python3
''' A Module That Define A Square'''


class Square:
    ''' A Class That Represents A Square'''

    def __init__(self, size=0):
        ''' Intializing The Class Square
        Args:
            size: The size Of The Square
        '''
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
        ''' Calculate Area Of The Square
        Return: The Current Square Area '''
        return self.__size ** 2

    def my_print(self):
        '''  prints in stdout the square with the character # '''
        if self.__size == 0:
            print("")
        [print("#" * self.__size) for i in range(self.__size)]
