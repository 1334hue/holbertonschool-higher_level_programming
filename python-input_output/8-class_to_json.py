#!/usr/bin/python3
"""Defines a Class-to-JSON serialization function."""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure."""
    return obj.__dict__
