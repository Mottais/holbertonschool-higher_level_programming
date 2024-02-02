#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        with open("./histo_err", "a") as file:
            print("AAA: {}".format(e), file=file)
        print("BBB: {}".format(e), file=sys.stderr)
        return False
