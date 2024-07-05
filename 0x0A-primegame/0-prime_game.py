#!/usr/bin/python3
'''Module for the prime game'''


def generatePrimes(x):
    '''Returns a list of prime numbers'''
    # step 1 generate primes using Sieve of Eratosthenes
    primes = []
    sieve = [True] * (x + 1)
    for i in range(2, x + 1):
        if sieve[i]:
            primes.append(i)
            for j in range(i, x + 1, i):
                sieve[j] = False
    return primes


def isWinner(x, nums):
    '''Returns the winner of the prime game'''
    # step 2 simulate Each round
    if not x or not nums:
        return None

    mScore = bScore = 0
    for i in range(x):
        primes = generatePrimes(nums[i])
        if len(primes) % 2 == 0:
            bScore += 1
        else:
            mScore += 1

    # step 3 determine winner
    if mScore > bScore:
        return "Maria"
    elif mScore < bScore:
        return "Ben"
    return None
