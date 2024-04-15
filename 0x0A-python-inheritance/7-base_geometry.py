#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry"""


class BaseGeometry:
    """Reprsent Base Geometry."""

    def area(self):
        """Not Yet Implemented"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer Validator"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
