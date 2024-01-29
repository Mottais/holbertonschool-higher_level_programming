#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_nex_list = list(my_list)
    if 0 <= idx < len(my_nex_list):
        my_nex_list[idx] = element
    return my_nex_list
