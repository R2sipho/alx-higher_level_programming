#!/usr/bin/python3
"""Module 2-is_same_class."""


def is_same_class(obj, a_class):
    """Check if obj is exactly an instance of the specified class.

    Args:
        - obj: object to check
        - a_class: specified class

    Returns:
        - True if obj is exactly an instance of the specified class,
          False otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
