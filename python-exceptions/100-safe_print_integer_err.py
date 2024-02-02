#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        # test export vers fichier
        # with open("./histo_err", "a") as file:
        #    print("Exception: {}".format(e), file=file)
        print("Exception: {}".format(e), file=sys.stderr)
        return False
