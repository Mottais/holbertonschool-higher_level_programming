#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    nb_arg = len(sys.argv) - 1

    if nb_arg == 0:
        print("0 arguments.")
    if nb_arg == 1:
        print("1 argument:")
    if nb_arg > 1:
        print("{} arguments:".format(nb_arg))

    for i in range(1, nb_arg + 1):
        print("{}: {}".format(i, sys.argv[i]))
