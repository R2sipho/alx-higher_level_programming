#!/usr/bin/python3
"""
This module implements a Rectangle object
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle implementation
    """

    def __init__(self, width: int, height: int, x=0, y=0, id=None):
        """Initialization
        """
        super().__init__(id)

        self._width = width
        self._height = height
        self._x = x
        self._y = y

    def __str__(self) -> str:
        """String representation
        """
        return "[Rectangle] ({}) {}/{} - {}/{}" \
            .format(self.id, self._x, self._y, self._width, self._height)

    def check_type_value(self, name: str, value: object, greater_equal=False):
        """Type and value validation
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if not greater_equal:
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        else:
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self) -> int:
        """Width getter
        """
        return self._width

    @width.setter
    def width(self, width: int):
        """Width setter
        """
        self.check_type_value('width', width)
        self._width = width

    @property
    def height(self) -> int:
        """Height getter
        """
        return self._height

    @height.setter
    def height(self, height: int):
        """Height setter
        """
        self.check_type_value('height', height)
        self._height = height

    @property
    def x(self) -> int:
        """X getter
        """
        return self._x

    @x.setter
    def x(self, x: int):
        """X setter
        """
        self.check_type_value('x', x, True)
        self._x = x

    @property
    def y(self) -> int:
        """Y getter
        """
        return self._y

    @y.setter
    def y(self, y: int):
        """Y setter
        """
        self.check_type_value('y', y, True)
        self._y = y

    def area(self) -> int:
        """Area
        """
        return self._width * self._height

    def display(self):
        """Prints # shape of the rectangle
        """
        print('\n' * self._y, end='')
        for _ in range(self._height):
            print(' ' * self._x + '#' * self._width)

    def update(self, *args, **kwargs):
        """Update rectangle attributes
        """
        expect = (self.id, self._width, self._height, self._x, self._y)
        if args != ():
            self.id, self._width, self._height, self._x, self._y = \
                args + expect[len(args):len(expect)]
        elif kwargs:
            for (name, value) in kwargs.items():
                setattr(self, name, value)

    def to_dictionary(self) -> int:
        """Rectangle to dictionary
        """
        return {
            'x': self._x, 'y': self._y, 'id': self.id,
            'height': self._height, 'width': self._width}

