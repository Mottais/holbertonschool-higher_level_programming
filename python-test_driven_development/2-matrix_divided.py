#!/usr/bin/python3
"""
this
is a
5 line comment
"""


def matrix_divided(matrix, div):
    """
    divide a matrix by div
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    message = "matrix must be a matrix (list of lists) of integers/floats"
    new_matrix = [[0.0] * len(matrix[0]) for _ in range(len(matrix))]
    for row in range(len(matrix)):
        if len(matrix[row]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for i in range(len(matrix[0])):
            if not isinstance(matrix[row][i], (int, float)):
                raise TypeError(message)
            new_matrix[row][i] = round(matrix[row][i] / div, 2)
    return (new_matrix)
