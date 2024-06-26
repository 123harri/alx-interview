#!/usr/bin/python3
"""
0. Pascal's Triangle
"""

def pascal_triangle(n):
    """
    Generates Pascal's triangle up to n rows.

    Args:
        n (int): Number of rows in Pascal's triangle.

    Returns:
        list of lists: Pascal's triangle as a list of lists of integers.
                       Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)  # Initialize row with 1s
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle

# Example usage:
if __name__ == "__main__":
    n = 5
    triangle = pascal_triangle(n)
    for row in triangle:
        print("[{}]".format(",".join(map(str, row))))
