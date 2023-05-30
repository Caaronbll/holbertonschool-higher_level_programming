#!/usr/bin/python3
"""Write a class Square that inherits from Rectangle
size: def __init__(self, size)"""


Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """Declaration"""
    def __init__(self, size):
        """initialization"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size