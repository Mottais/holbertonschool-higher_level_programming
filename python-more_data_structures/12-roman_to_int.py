#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return 0

    roman_int = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    roman_value, prec = 0, 0

    for c in roman_string:
        if prec < roman_int.get(c):
             roman_value -= 2 * prec
        roman_value += roman_int.get(c)
        prec = roman_int.get(c)
    return roman_value
