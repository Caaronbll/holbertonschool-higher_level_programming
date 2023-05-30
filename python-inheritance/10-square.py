#!/usr/bin/python3
"""Square class that inherits from Rectangle (9-rectangle.py)
Instantiation with size: def __init__(self, size)
size must be private. No getter or setter
size must be a positive integer, validated by integer_validator
the area() method must be implemented
print() should print, and str() should return, the square description:
[Square] <width>/<height>"""

Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """Declaration of Square class"""
    def __init__(self, size):
        """initialization"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size