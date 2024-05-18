#!/usr/bin/python3
"""
This module defines a class Square with private instance attributes size and
position, and methods to calculate area and print the square.
"""


class Square:
    """
    Defines a square by:
        - size: private instance attribute
        - position: private instance attribute
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance.

        Args:
            size (int): size of the square (default is 0)
            position (tuple): position of the square (default is (0, 0))
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for size attribute.

        Returns:
            int: size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size attribute.

        Args:
            value (int): size to set

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter method for position attribute.

        Returns:
            Tuple: Position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for position attribute.

        Args:
            Value (tuple): position to set

        Raises:
            TypeError: If value is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(i, int) for i in value) \
                or not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            Area of the square
        """
        return self.size ** 2

    def my_print(self):
        """
        Prints the square to stdout.
        """
        if self.size == 0:
            print()
            return
        for _ in range(self.position[1]):
            print()
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
