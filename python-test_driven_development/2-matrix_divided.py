#!/usr/bin/python3
"""dividing a matrix"""


def matrix_divided(matrix, div):
    if type(matrix) is not int or float:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for i in matrix:
        if len(matrix[0]) != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int or float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for row in matrix:
        for col in matrix[row]:
            new_matrix[row][col] = float(matrix[row][col] / 2)

    return new_matrix