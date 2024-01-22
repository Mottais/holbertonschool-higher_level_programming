#!/usr/bin/python3
for dec in range(10):
    for unit in range(dec, 10):
        if dec != unit:
            if not(dec == 8 and unit == 9):
                print("{}{}, ".format(dec, unit), end=", ")
print("89")
