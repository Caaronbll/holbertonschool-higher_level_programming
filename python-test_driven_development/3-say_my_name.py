#!/usr/bin/python3
"""
says first and last name based on 2 string inputs
"""


def say_my_name(first_name, last_name=""):
    """Makes sure both inputs are strings and prints them"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
