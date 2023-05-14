#!/usr/bin/python3
def no_c(my_string):
    new_string = ''
    for i in range(len(my_string)):
        if my_string[i] != 'c' and my_string != 'C':
            new_string += my_string[i:(1 + i)]
    return new_string