#!/usr/bin/python3
"""Rectangle Module

Defines a Rectangle class with width, height, area, perimeter,
deletion, and comparison attributes.
"""


class Rectangle:
    """Representation of a geometric rectangle."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Return a string representation of the rectangle using '#' characters."""
        if self.height == 0 or self.width == 0:
            return ''
        rectangle_str = (str(self.print_symbol) * self.width + '\n') * self.height
        return rectangle_str.rstrip('\n')

    def __repr__(self):
        """Return a string representation of a Rectangle instance.

        This representation can recreate a new instance using eval().
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Delete a Rectangle instance."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The width value, must be non-negative.
        """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The height value, must be non-negative.
        """
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.__width + self.__height) if self.height != 0 and self.width != 0 else 0

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Find the biggest Rectangle based on the area.

        Args:
            rect_1 (Rectangle): Rectangle instance.
            rect_2 (Rectangle): Rectangle instance different from rect_1.

        Returns:
            The instance with the biggest area,
            or rect_1 if both rectangles have the same area.
        """
        if not isinstance(rect_1, Rectangle) or not isinstance(rect_2, Rectangle):
            raise TypeError("Both rect_1 and rect_2 must be instances of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

