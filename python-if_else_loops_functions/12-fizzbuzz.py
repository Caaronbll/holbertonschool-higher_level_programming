#!/usr/bin/python3
def fizzbuzz():
    i = 1
    for i in range(101):
        if i % 3 and 1 % 5 is 0:
            print("FizzBuzz", end=' ')
        elif i % 3 == 0:
            print("Fizz", end=' ')
        elif i % 5 == 0:
            print("Buzz", end=' ')
        else:
            print(i, end=' ')
