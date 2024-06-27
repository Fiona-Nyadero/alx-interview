#!/usr/bin/python3
'''Module for Island Perimeter'''


def island_perimeter(grid):
    '''Returns the perimeter of the Grid Island'''
    perimeter = 0

    for row in range(len(grid)):
        for i in range(len(grid[row])):
            if grid[row][i] == 1:
                perimeter += 4

                if row > 0 and grid[row-1][i] == 1:
                    perimeter -= 2
                if i > 0 and grid[row][i-1] == 1:
                    perimeter -= 2

    return perimeter
