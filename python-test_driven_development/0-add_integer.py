#!/usr/bin/python3
"""
Adds two integers and makes sure both integers
are integers or floats before they are added.
"""
def add_integer(a, b=98):
    if type(a) is not float or type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not float or type(b) is not int:
        raise TypeError("b must be an integer")
    a_int = int(a)
    b_int = int(b)
    return a_int + b_int
