#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    t = (len(my_list) - 1)
    while t >= 0:
        print(f"{my_list[t]}")
        t = t - 1
