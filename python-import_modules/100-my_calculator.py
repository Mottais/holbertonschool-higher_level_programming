#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv
    if len(argv) != 4:
        print("Usage:", argv[0], "<a> <operator> <b>")
        exit(1)

    from calculator_1 import add, sub, div, mul
    a, op, b = int(argv[1]), argv[2], int(argv[3])

    if op == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif op == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif op == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
    elif op == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
