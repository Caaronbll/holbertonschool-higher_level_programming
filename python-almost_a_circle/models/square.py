#!/usr/bin/python3
"""
Write the class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """initializing Square Class"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns information about the square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"