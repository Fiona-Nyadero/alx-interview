#!/usr/bin/python3
'''Module rotates a 2d matrix by 90degree'''


def rotate_2d_matrix(matrix):
    '''fx rotates an nxn matrix by 90 degrees clockwise'''

    n = len(matrix)
    for f in range(n):
        for g in range(f+1, n):
            matrix[f][g], matrix[g][f] = matrix[g][f], matrix[f][g] 

    for row in matrix:
        row.reverse()
