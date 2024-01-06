#!/usr/bin/python3
"""
Module matrix_divided
Defines a matrix division function.
"""

def matrix_divided(matrix, divisor):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list): A list of lists containing integers or floats.
        divisor (int/float): The divisor for the matrix elements.

    Raises:
        TypeError: If the matrix or divisor is not valid.
        ZeroDivisionError: If divisor is 0.

    Returns:
        list: A new matrix representing the result of the division.
    """

    
    if not is_valid_matrix(matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

   
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    
    if not is_valid_number(divisor):
        raise TypeError("divisor must be a number")
    if divisor == 0:
        raise ZeroDivisionError("division by zero")

    
    result_matrix = [
        [round(element / divisor, 2) for element in row]
        for row in matrix
    ]

    return result_matrix

def is_valid_matrix(matrix):
    """
    Check if the matrix is valid (list of lists containing integers or floats).
    """
    return (
        isinstance(matrix, list) and matrix and
        all(isinstance(row, list) for row in matrix) and
        all(isinstance(ele, (int, float)) for row in matrix for ele in row)
    )

def is_valid_number(num):
    """
    Check if the number is a valid integer or float.
    """
    return isinstance(num, (int, float))
