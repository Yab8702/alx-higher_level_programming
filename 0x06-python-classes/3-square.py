#!/usr/bin/python3
''' A Module That Define A Square'''


class Square:
    '''A Class That Represents A Square'''

    def __init__(self, size=0):
        ''' Intializing The Class Square
        Args:
            size: The size Of The Square
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        ''' Calculate Area Of The Square
        Return: The Current Square Area '''
        return self.__size ** 2
