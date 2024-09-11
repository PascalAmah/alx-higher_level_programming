#!/usr/bin/python3

def islower(c):
    """Function checks for lowercase characters."""
    if ord('a') <= ord(c) <= ord ('z'):
        return True
    else:
        return False
