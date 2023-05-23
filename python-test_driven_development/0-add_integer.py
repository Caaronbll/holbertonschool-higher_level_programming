#!/usr/bin/python3
"""
Adds two integers and makes sure both integers
are integers or floats before they are added.
"""


def add_integer(a, b=98):
    if type(a) is not int:
        if type(a) is float:
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    if type(b) is not int:
        if type(b) is float:
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    return a + b