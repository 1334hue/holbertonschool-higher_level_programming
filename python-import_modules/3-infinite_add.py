#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total = 0
    # Iterate through all arguments skipping the program name at index 0
    for arg in sys.argv[1:]:
        total += int(arg)

    print("{}".format(total))
