#!/usr/bin/python3
"""
Rectangle Class with public class attributes,
private instance attributes (width, height),
public methods, special methods, static methods, and class methods
"""

class Rectangle:
    """Rectangle Class with attributes and methods."""
    
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def area(self):
        """Calculate the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the Rectangle."""
        return 2 * (self.__width + self.__height) if self.__width and self.__height else 0

    def __str__(self):
        """Return a string representation of the Rectangle."""
        if not self.__width or not self.__height:
            return ""
        return '\n'.join([str(self.print_symbol) * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Return an “official” string representation of the Rectangle."""
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """Print a message when a Rectangle instance is deleted."""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Getter for the width property."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width property."""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Getter for the height property."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height property."""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on the area."""
        if not all(isinstance(rect, Rectangle) for rect in (rect_1, rect_2)):
            raise TypeError("Both rect_1 and rect_2 must be instances of Rectangle")

        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Create a square Rectangle."""
        return cls(size, size)

