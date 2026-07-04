#!/usr/bin/python3
"""Defines a function that saves a Python object to a file using JSON."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
