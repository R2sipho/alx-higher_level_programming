#!/usr/bin/python3
"""Rectangle Module

This module defines the Rectangle class representing a geometric rectangle.
"""


class Rectangle:
    """Rectangle class with width, height, area, and perimeter attributes."""

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.width = width
        self.height = height

    def __str__(self):
        """Return a string representation of the rectangle filled with '#' characters."""
        if self.height == 0 or self.width == 0:
            return ''
        rectangle_str = ('#' * self.width + '\n') * self.height
        return rectangle_str[:-1]

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): Width value, must be a non-negative integer.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): Height value, must be a non-negative integer.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.__width + self.__height)

