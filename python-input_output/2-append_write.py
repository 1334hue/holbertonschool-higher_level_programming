#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to a UTF8 text file and returns chars added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
