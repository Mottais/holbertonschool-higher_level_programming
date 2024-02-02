#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    ele_to_del = []
    for x, y in a_dictionary.items():
        if y == value:
            ele_to_del.append(x)

    for x in ele_to_del:
        del a_dictionary[x]
    return a_dictionary
