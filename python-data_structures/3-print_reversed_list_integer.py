#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    t = (len(my_list) - 1)
    if t < 0:
        return None
    while t >= 0:
        print("{:d}".format(my_list[t]))
        t = t - 1