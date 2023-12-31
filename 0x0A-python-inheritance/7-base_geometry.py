#!/usr/bin/python3
"""Module 7-base_geometry.
Creates  BaseGeometry class.
"""
class BaseGeometry:
    """Class with area and integer_validator methods."""

    def area(self):
        """Raise an exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the value.

        Args:
            - name: a string (assumed to be always a string)
            - value: the value to be validated

        Raises:
            - TypeError: if the value is not an integer
            - ValueError: if the value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
