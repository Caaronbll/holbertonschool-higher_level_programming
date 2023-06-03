#!/usr/bin/python3
"""Write the first class Base"""


class Base():
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.__id = id
        else:
            __nb_objects += 1