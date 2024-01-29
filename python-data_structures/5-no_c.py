#!/usr/bin/python3
def no_c(my_string):
    my_new_string = ''
    for cararc in my_string:
        if cararc not in 'Cc':
            my_new_string += cararc
    return my_new_string
