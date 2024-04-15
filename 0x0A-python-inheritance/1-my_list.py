#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements MyList Class"""

    def print_sorted(self):
        """Print a sorting list"""

        print(sorted(self))
