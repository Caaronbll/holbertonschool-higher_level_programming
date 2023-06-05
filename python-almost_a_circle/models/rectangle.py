#!/usr/bin/python3
"""
Write the class Rectangle that inherits from Base
"""
Base = __import__('base.py').Base


class Rectangle(Base):
    """rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """named module"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width setter"""
        return self.__width

    @property
    def height(self):
        """height setter"""
        return self.__height

    @property
    def x(self):
        """y setter"""
        return self.__x

    @property
    def y(self):
        """x setter"""
        return self.__y