#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    liste_c = [0, 0]
    for i in range(len(tuple_a)):
        liste_c[i] += tuple_a[i]
    for i in range(len(tuple_b)):
        liste_c[i] += tuple_b[i]

    return(tuple(liste_c))
