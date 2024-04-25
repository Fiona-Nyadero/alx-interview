#!/usr/bin/python3
''''''


def minOperations(n: int) -> int:
    ''''''
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
