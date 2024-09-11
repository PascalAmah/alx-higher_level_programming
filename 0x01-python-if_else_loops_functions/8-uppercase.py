#!/usr/bin/python3

def uppercase(s):
    """Prints a string in uppercase followed by a new line."""

    for c in s:
        if ord('a') <= ord(c) <= ord('z'):
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
