#!/usr/bin/python3

def uppercase(str):
    asci = 0
    for i in range(len(str)):
        asci = ord(str[i])
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            asci -= 32
        print("{}".format(chr(asci)), end='')
    print()
