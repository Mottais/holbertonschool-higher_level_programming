#!/usr/bin/python3
if __name__ == "__main__":

    import sys
    test_etoile = sys.argv[0] in sys.argv[1:]
    if test_etoile:
        sys.argv[2] = '*'

    from calculator_1 import add, sub, div, mul
    a, op, b = int(sys.argv[1]), sys.argv[2], int(sys.argv[len(sys.argv)-1])

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
