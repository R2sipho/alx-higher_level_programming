#!/usr/bin/python3
"""Module 4-inherits_from."""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a class that inherited from a_class.

    Args:
        - obj: object to check
        - a_class: specified class

    Returns:
        - True if obj is an instance of a class that inherited from a_class,
          False otherwise.
    """
    return issubclass(type(obj), a_class)

