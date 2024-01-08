#!/usr/bin/python3
"""Module 3-is_kind_of_class."""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of, or if obj inherited from, a_class.

    Args:
        - obj: object to check
        - a_class: specified class

    Returns:
        - True if obj is an instance of, or if obj inherited from, a_class,
          False otherwise.
    """
    return isinstance(obj, a_class)

