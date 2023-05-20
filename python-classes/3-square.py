#!/usr/bin/python3
"""Square Class set-up"""


class Square:
    """Declaring Square Class"""
    def __init__(self, size=0):
        """Declaring size attribute"""
        self.__size = size
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        """Declaring area method"""
        return self.__size * self.__size
