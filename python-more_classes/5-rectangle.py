#!/usr/bin/python3
"""This module defines a class Rectangle that defines a rectangle"""


class Rectangle:
    """This class defines a rectangle by its width and height"""

    def __init__(self, width=0, height=0):
        """Initialize new Rectangle instance with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle
        If width or height is equal to 0, the perimeter is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle
        If width or height is equal to 0, return an empty string
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Return a string representation of
        the rectangle to recreate a new instance"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
