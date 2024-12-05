#!/usr/bin/python3
"""
function that returns the perimeter of the island described in grid
"""

def island_perimeter(grid):
    """
    Args:
        grid: List of integers (0 is water, 1 is land)

    Returns:
        int: The perimeter of the island
    """

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            # check if it is a Land cell
            if grid[i][j] == 1:
                # start with 4 sides
                perimeter += 4

                #checking if the 4 sides are within grid bound
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1
                if i < rows -1 and grid[i + 1][j] == 1:
                    perimeter -= 1
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1
                if j < cols -1 and grid[i][j + 1] == 1:
                    perimeter -= 1
    return perimeter