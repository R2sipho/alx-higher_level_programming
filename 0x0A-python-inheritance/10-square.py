#!/usr/bin/python3
"""Module 10-square."""

class BaseGeometry:
    """Represents the base geometry class."""

    def area(self):
        """Raises an exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value.

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


class Rectangle(BaseGeometry):
    """Represents a rectangle."""

    def __init__(self, width, height):
        """Initializes the rectangle.

        Args:
            - width: width of the rectangle
            - height: height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Computes the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a formatted string."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initializes a Square.

        Args:
            - size: size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Computes the area of a Square instance."""
        return self.__size ** 2

    def __str__(self):
        """Returns a formatted string."""
        return "[Square] {}/{}".format(self.__size, self.__size)

