#!/usr/bin/python3
"""
Square class that inherits from Rectangle
"""

Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """Declaration of Square class"""
    def __init__(self, size):
        """initialization"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size