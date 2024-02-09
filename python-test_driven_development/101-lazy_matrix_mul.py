#!/usr/bin/python3
"""
matrix_mul function
function that multiplies 2 matrices m_a an m_b
If m_a an m_b can’t be multiplied:
raise a Error exception with a message
"""


import numpy as np

def lazy_matrix_mul(m_a, m_b):

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not m_a or not m_a[0]:
        raise ValueError("m_a can't be empty")
    if not m_b or not m_b[0]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        if not all(isinstance(val, (int, float)) for val in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(val, (int, float)) for val in row):
            raise TypeError("m_b should contain only integers or floats")

    if any(len(row) != len(m_a[0]) for row in m_a[1:]):
        raise TypeError("each row of m_a must be of the same size")
    if any(len(row) != len(m_b[0]) for row in m_b[1:]):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    # Convertir les listes en tableaux NumPy
    m_a = np.array(m_a)
    m_b = np.array(m_b)

    # Vérifier si les tableaux ont le bon format
    if m_a.ndim != 2:
        raise ValueError("m_a must be a list of lists")
    if m_b.ndim != 2:
        raise ValueError("m_b must be a list of lists")

    if m_a.shape[1] != m_b.shape[0]:
        raise ValueError("m_a and m_b can't be multiplied")

    # Effectuer la multiplication de matrices
    result = np.dot(m_a, m_b)

    # Convertir le tableau NumPy résultant en liste Python
    return result.tolist()
