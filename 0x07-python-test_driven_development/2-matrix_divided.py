#!/usr/bin/python3

def matrix_divided(matrix, div):
    for row in matrix:
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
            if not isinstance(row, list):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
    row_size = set(len(row) for row in matrix)
    if len(row_size) > 1:
        raise TypeError("Each row of matrix must have the same length")
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(num / div, 2) for num in row] for row in matrix]
