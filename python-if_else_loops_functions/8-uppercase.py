#!/usr/bin/python3
def uppercase(str):
    for c in str:
        # Check if ASCII value falls under lowercase 'a' (97) to 'z' (122)
        if 97 <= ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print()
