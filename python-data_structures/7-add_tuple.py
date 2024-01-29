#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    liste_c = list(tuple_a)
    for i in range(2):
        if i < len(tuple_b):
            liste_c[i] = tuple_a[i] + tuple_b[i]
        else:
            liste_c[i] = tuple_a[i]
    return(tuple(liste_c))
