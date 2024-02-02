#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    try:
        return (a ** b)
    except Exception:
        print('Too far')
        return (a + b)
