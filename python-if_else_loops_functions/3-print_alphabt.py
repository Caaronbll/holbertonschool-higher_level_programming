#!/usr/bin/python3
for alpha_letters in range(97, 123):
    if alpha_letters != 101 and alpha_letters != 113:
        print("{0}".format(chr(alpha_letters)), end='')
