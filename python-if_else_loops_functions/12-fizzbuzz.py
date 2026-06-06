#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end="")
        elif i % 3 == 0:
            print("Fizz", end="")
        elif i % 5 == 0:
            print("Buzz", end="")
        else:
            print("{}".format(i), end="")
        
        # Add space unless it's the last element
        if i < 100:
            print(" ", end="")
    print()
