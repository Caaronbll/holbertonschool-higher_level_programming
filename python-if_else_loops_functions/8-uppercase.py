#!/usr/bin/python3

def uppercase(str):
    asci = 0
    i = 0
    while str[i]:
        asci = ord(str[i])
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            asci -= 32
        print("{chr(asci)}", end='')
    print()
