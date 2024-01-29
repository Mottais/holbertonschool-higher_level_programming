#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    new_matrix = []

    for row in matrix:
        new_row = []
        for value in row:
            new_row.append(value ** 2)
        new_matrix.append(new_row)

    return new_matrix
    # 2 autres solutions : compréhension
    # return ([list(map(lambda x: x ** 2, row)) for row in matrix])
    # return [[x ** 2 for x in row] for row in matrix]
