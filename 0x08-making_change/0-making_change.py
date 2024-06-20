#!/usr/bin/python3
'''Module for making change fx'''


def makeChange(coins, total):
    '''Returns fewest no. of coins needed to meet total'''

    if total < 1:
        return 0

    coins.sort(reverse=True)

    dp = 0

    for coin in coins:
        if total == 0:
            break
        amount = total // coin
        total -= amount * coin
        dp += amount

    return dp if total == 0 else -1
