#!/usr/bin/python3
"""
This module defines a function that calculates the perimeter of an island
represented in a grid. The grid is a list of lists where 1 represents land
and 0 represents water. The function assumes that the grid is completely
surrounded by water and contains only one island.
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in the grid.

    Parameters:
    grid (list of list of int): A rectangular grid where 1 represents land
    and 0 represents water.

    Returns:
    int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
