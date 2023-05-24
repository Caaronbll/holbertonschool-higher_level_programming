#!/usr/bin/python3
"""
writing a rectangle class
"""


class Rectangle:
    """Declaring a Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter for width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width property"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter for height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height property"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Public instance method Area"""
        return self.__height * self.__width

    def perimeter(self):
        """Public instance method perimeter"""
        if self.__width == 0:
            return 0
        elif self.__height == 0:
            return 0
        else:
            p = (self.__width + self.__height) * 2
            return p

    def __str__(self):
        string = ""
        if self.height > 0 and self.height > 0:
            for row in range(self.height):
                for col in range(self.width):
                    string += str(self.print_symbol)
                if row < self.height - 1:
                    string += '\n'
            return string
        else:
            return string

    def __repr__(self) -> str:
        """repr/eval function "giver" """
        return f"Rectangle({self.__width}, {self._height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
