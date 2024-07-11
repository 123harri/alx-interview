#!/usr/bin/python3
"""
Calculates the minimum number of operations
needed to achieve exactly n 'H' characters
in a text file using Copy All and Paste operations.
"""


def minOperations(n):
    if n <= 1:
        return n

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations


if __name__ == "__main__":
    n = 4
    print(f"Min # of operations to reach {n} char: {minOperations(n)}")

    n = 12
    print(f"Min # of operations to reach {n} char: {minOperations(n)}")
