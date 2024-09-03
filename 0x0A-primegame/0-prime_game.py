#!/usr/bin/python3
"""
Prime Game: Determines the winner of the game based on prime number choices.
"""


def isWinner(x, nums):
    """
    Determines the winner after x rounds of a prime number game.

    Arguments:
    x -- the number of rounds
    nums -- an array where each element is 'n',
    the upper limit of numbers in the round

    Returns:
    The name of the player that won the most rounds (either "Maria" or "Ben").
    If the winner cannot be determined, returns None.
    """
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False

    # Sieve of Eratosthenes to find all primes up to max_n
    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False

    primes_count = [0] * (max_n + 1)

    for i in range(1, max_n + 1):
        primes_count[i] = primes_count[i - 1] + (1 if sieve[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if primes_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
