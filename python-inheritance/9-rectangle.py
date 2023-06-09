#!/usr/bin/python3
"""
Write a class Rectangle that inherits from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class declaration"""
    def __init__(self, width, height):
        """initiation"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area method"""
        return self.__width * self.__height

    def __str__(self):
        """str method"""
        return f"[Rectangle] {self.__width}/{self.__height}"
