#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda row: list(map(lambda x: x * x, row)), matrix))
    # return [ [x * x for x in ligne] for ligne in matrix]
