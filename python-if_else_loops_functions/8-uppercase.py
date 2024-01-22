#!/usr/bin/python3
def uppercase(texte):
    result = 0
    for c in texte:
        if ord('a') <= ord(c) <= ord('z'):
            c = chr(ord(c) - ord('a') + ord('A'))
        print("{}".format(c), end="")
    print("")
    return
