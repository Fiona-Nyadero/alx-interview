#!/usr/bin/python3
'''Module gets the min no. of copy and paste'''


def minOperations(n: int) -> int:
    '''Function calculate the min no of operations'''
    if n <= 1:
        return 0
    opertns = 0
    divr = 2
    while n > 1:
        if n % divr == 0:
            n //= divr
            opertns += divr
        else:
            divr += 1
    return opertns
