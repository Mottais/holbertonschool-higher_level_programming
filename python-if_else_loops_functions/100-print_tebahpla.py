#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(i - i % 2 * 32)), end="")
