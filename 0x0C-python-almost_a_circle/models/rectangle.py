#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): Width of the new Rectangle.
            height (int): Height of the new Rectangle.
            x (int): x-coordinate of the new Rectangle.
            y (int): y-coordinate of the new Rectangle.
            id (int): Identity of the new Rectangle.
        Raises:
            TypeError: If width or height is not an int.
            ValueError: If width or height <= 0.
            TypeError: If x or y is not an int.
            ValueError: If x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("Width must be an integer")
        if value <= 0:
            raise ValueError("Width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("Height must be an integer")
        if value <= 0:
            raise ValueError("Height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get/set the x-coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x-coordinate must be an integer")
        if value < 0:
            raise ValueError("x-coordinate must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get/set the y-coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y-coordinate must be an integer")
        if value < 0:
            raise ValueError("y-coordinate must be >= 0")
        self.__y = value
