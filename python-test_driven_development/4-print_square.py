#!/usr/bin/python3
"""Prints a square of a size input"""


def print_square(size):
    """prints a square the size you want"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float:
        if size < 0:
            raise TypeError("size must be an integer")
        else:
            size = int(size)

    for i in range(size):
        print("#" * size)
