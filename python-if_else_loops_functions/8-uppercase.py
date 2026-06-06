#!/usr/bin/python3
def to_uppercase(str):
    for c in str:
        # Check if character is lowercase, if so convert to uppercase using ASCII
        if 97 <= ord(c) <= 122:
            print("{}".format(chr(ord(c) - 32)), end="")
        else:
            print("{}".format(c), end="")
    print()
