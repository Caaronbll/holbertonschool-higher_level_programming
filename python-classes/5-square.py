#!/usr/bin/python3
"""Square Class set-up"""


class Square:
    """Declaring Square Class"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    def area(self):
        return self.__size * self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
