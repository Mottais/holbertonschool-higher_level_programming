#!/usr/bin/

def remove_char_at(str, n):
    for i in range(len(str)):
        if i != n:
            print(str[i], end="")
    return ""
