#!/usr/bin/python3
"""
Write a class Student
that defines a student by
"""


class Student():
    """declaring student class"""
    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def to_json(self):
        """retrieves dictionary representation of Student"""
        return self.__dict__
