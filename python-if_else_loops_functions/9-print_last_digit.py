#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        lstNum = number % 10
    if number < 0:
        lstNum = number % -10
    print(f"{lstNum}", end='')
    return(lstNum)
