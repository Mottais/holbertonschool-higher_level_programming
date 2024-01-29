#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list):
        my_list[idx:idx + 1] = []
        # autres solutions :
        # my_list.remove(my_list[idx])
        # del my_list[idx]
    return my_list
