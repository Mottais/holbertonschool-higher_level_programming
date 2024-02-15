#!/usr/bin/python3
"""Definition of function pascal triangle"""


def pascal_triangle(n):
    """ Create a function that returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    if n <= 0:
        return []

    list_num = [[1]]

    if n >= 2:
        list_num = [[1], [1, 1]]

    for i in range(1, n - 1):
        new_line = [1]
        for j in range(0, i):
            new_line.append(list_num[i][j] + list_num[i][j + 1])
        new_line.append(1)
        list_num.append(new_line)
    return list_num
