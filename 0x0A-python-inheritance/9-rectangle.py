#!/usr/bin/python3
"""Module 9-rectangle.
Creates a Rectangle class.
"""

from typing import Union


class BaseGeometry:
    """Base class for geometry."""

    def area(self) -> None:
        """Raises an exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name: str, value: int) -> None:
        """Validates the value.

        Args:
            - name: a string (assumed to be always a string)
            - value: the value to be validated

        Raises:
            - TypeError: if the value is not an integer
            - ValueError: if the value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Represents a rectangle.

    Private instance attributes:
        - width
        - height
    Public method area().
    Inherits from BaseGeometry.
    """

    def __init__(self, width: int, height: int) -> None:
        """Initializes instance.

        Args:
            - width: width of the rectangle
            - height: height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self) -> str:
        """Returns a formatted string."""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self) -> int:
        """Computes the area of the Rectangle instance.
        Overwrites the area() method from BaseGeometry.
        """
        return self.__width * self.__height

