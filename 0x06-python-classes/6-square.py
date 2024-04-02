#!/usr/bin/python3
''' A Module That Define A Square'''


class Square:
    ''' A Class That Represents A Square'''

    def __init__(self, size=0, position=(0, 0)):
        ''' Intializing The Class Square
        Args:
            size: The size Of The Square
            position: The Position Of A Square
        '''
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        ''' Calculate Area Of The Square
        Return: The Current Square Area '''
        return self.__size ** 2

    def my_print(self):
        '''  prints in stdout the square with the character # '''
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for i in range(self.__position[0])]
            [print("#", end="") for i in range(self.__size)]
            print("")
