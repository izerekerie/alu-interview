#!/usr/bin/python3
"""
0-pascal_triangle.py

This module contains a function `pascal_triangle(n)` that generates
Pascal's triangle of size `n`. The triangle is represented as a list of lists,
where each list corresponds to a row in the triangle.

Functions:
    pascal_triangle(n): Returns the Pascal's triangle of `n` as a list of lists.
"""

def pascal_triangle(n):
    """Returns a list of lists representing the Pascal's triangle of size n.

    Args:
        n (int): The size of the Pascal's triangle.

    Returns:
        list: A list of lists of integers representing the Pascal's triangle of n.
              An empty list is returned if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row of Pascal's triangle

    for i in range(1, n):
        row = [1]  # Every row starts with 1
        for j in range(1, i):
            # Each element is the sum of the two elements directly above it
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # Every row ends with 1
        triangle.append(row)

    return triangle
