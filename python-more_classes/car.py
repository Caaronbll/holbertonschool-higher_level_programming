#!/usr/bin/python3

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return '__str__ for car'

    def __repr__(self):
        return '__repr__ for car'


my_car = Car("red", 57300)

print(my_car)
my_car
'{}'.format(my_car)
