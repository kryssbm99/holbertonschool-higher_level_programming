#!/usr/bin/python3
"""
Function Divides all elements of a matrix by a given number.
"""


def matrix_divided(matrix, div):
    """
    This function takes a matrix (list of lists) of integers or floats and divides all elements by a given number.
    Each row of the matrix must be of the same size.
    The divisor 'div' must be a non-zero number (integer or float).
    """

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    row_lengths = set(len(row) for row in matrix)
    if len(row_lengths) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix
