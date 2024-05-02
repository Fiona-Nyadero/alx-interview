#!/usr/bin/python3
'''An interpretation of Pascal's triangle of n '''


def pascal_triangle(n):
    '''returns a lists of int(s)'''
    if n <= 0:
        return []

    Pas_triangle = []
    for ln in range(n):
        line = [1]
        for r in range(1, ln):
            line.append(Pas_triangle[ln-1][r-1] + Pas_triangle[ln-1][r])
        if ln > 0:
            line.append(1)
        Pas_triangle.append(line)

    return Pas_triangle
