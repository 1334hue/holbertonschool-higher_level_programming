#!/usr/bin/python3
def uppercase(str):
    for char in str:
        # Check if character is lowercase using ASCII values
        if ord(char) >= 97 and ord(char) <= 122:
            # Subtract 32 to get uppercase equivalent
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")
