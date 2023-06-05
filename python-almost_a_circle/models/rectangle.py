#!/usr/bin/python3
"""
Write the class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(id)
        self.validate_integer("width", width, False)
        self.validate_integer("height", height, False)
        self.validate_integer("x", x, True)
        self.validate_integer("y", y, True)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value, True)
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer("y", value, True)
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        """method to validate the integer"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if eq and value < 0:
            raise ValueError(f"{name} must be >= 0")
        elif not eq and value <= 0:
            raise ValueError(f"{name} must be > 0")

    def area(self):
        """returns the area of the rectangle"""
        return self.__height * self.__width