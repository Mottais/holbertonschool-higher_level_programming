#!/usr/bin/python3
def common_elements(set_1, set_2):
    return {element for element in set_1 if element in set_2}
    # autre solution
    # return set_1.intersection(set_2)
