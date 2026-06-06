#!/usr/bin/python3
def print_last_digit(number):
    # Handle negative numbers correctly to find the absolute last digit
    last_digit = abs(number) % 10
    print("{}".format(last_digit), end="")
    return last_digit
