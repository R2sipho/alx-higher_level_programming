#!/usr/bin/python3
"""Module 3-rectangle
Defines a Rectangle class.
"""
class Rectangle:
    """Rectangle class defined by width and height."""

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.width = width
        self.height = height

    def __str__(self):
        """Return a string representation of a Rectangle instance filled with '#'.

        Returns:
            str: String representation of the rectangle.
        """
        if self.__height == 0 or self.__width == 0:
            return ''
        rectangle_str = ''
        for _ in range(self.__height):
            rectangle_str += '#' * self.__width + '\n'
        return rectangle_str.rstrip('\n')

    def __repr__(self):
        """Return an unambiguous string representation of a Rectangle instance.

        Returns:
            str: Unambiguous string representation.
        """
        return f"Rectangle(width={self.__width}, height={self.__height})"

    @property
    def width(self):
        """Retrieve the width of a Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of a Rectangle instance.

        Args:
            value (int): Value of the width, must be a positive integer.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of a Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of a Rectangle instance.

        Args:
            value (int): Value of the height, must be a positive integer.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of a Rectangle instance.

        Returns:
            int: Area of the rectangle, given by height * width.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of a Rectangle instance.

        Returns:
            int: Perimeter of the rectangle, given by 2 * (height + width).
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

