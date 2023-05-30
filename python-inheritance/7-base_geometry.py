#!/usr/bin/python3
"""Write an empty class BaseGeometry"""


class BaseGeometry():
    """class declaration"""

    def area(self):
        """area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        elif type(name) is not str:
            raise TypeError(f"{name} must be a string")
