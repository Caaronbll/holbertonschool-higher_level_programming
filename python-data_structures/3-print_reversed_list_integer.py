#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if type(my_list) is list:
        reverse(my_list)
        for i in my_list:
            print("{:d}".format(i))