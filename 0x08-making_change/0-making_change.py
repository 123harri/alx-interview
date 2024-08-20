#!/usr/bin/python3
"""
This module defines a function to calculate the fewest number of coins
needed to meet a given total amount.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet the given total.

    Parameters:
    coins (list): List of coin denominations.
    total (int): The total amount to be met.

    Returns:
    int: Fewest number of coins needed to meet total,
         -1 if total cannot be met by any number of coins.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
