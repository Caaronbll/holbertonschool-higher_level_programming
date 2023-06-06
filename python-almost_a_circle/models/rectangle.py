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

    def __str__(self):
        """returns information of this rectangle"""
        s= f"[Rectangle] ({self.id}) {self.x}/{self.y}"
        j = f"- {self.width}/{self.height}"
        return s+j

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

    def update(self, *args, **kwargs):
        """updates attributes with and without keywords"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """updates the attributes"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def area(self):
        """returns the area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """prints in stdout the rectangle made of #"""
        img = '#'
        if self.y > 0:
            j = '\n' * (self.y - 1)
            print(j)
        for i in range(self.__height):
            print(' ' * self.__x + img * self.__width)

    def to_dictionary(self):
        """returns a dictionary about the class"""
        return {"id": self.id, "width": self.__width,
                "height": self.__height, "x": self.__x, "y": self.__y}
