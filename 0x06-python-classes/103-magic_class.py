#!/usr/bin/python3
''' Define A Magic Class '''


import math


class MagicClass:
    ''' Represent the MagicClass '''

    def __init__(self, radius=0):
        ''' Initializing the MagicClass'''
        self.__radius = 0
        if (type(radius) is not int and type(radius) is not float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        ''' calculate the area'''
        return math.pi * self.__radius ** 2

    def circumference(self):
        ''' calculate circumference'''
        return 2 * math.pi * self.__radius
