#!/usr/bin/python3
"""Defines a class MyInt  inherits from int."""


class MyInt(int):
    """Define MyInt"""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
