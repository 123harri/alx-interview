#!/usr/bin/python3
"""
Calculates the minimum number of operations needed to
achieve exactly n 'H' characters
in a text file using Copy All and Paste operations.
"""

import math


def minOperations(n):
    """
    minOperations
    Gets fewest # of operations needed to result in exactly n H characters
    """
    if n <= 1:
        return n

    min_ops = float('inf')

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            min_ops = min(min_ops, i + minOperations(n // i))

    if min_ops == float('inf'):
        min_ops = n

    return min_ops


if __name__ == "__main__":
    n = 4
    print(f"Min # of operations to reach {n} char: {minOperations(n)}")

    n = 12
    print(f"Min # of operations to reach {n} char: {minOperations(n)}")
