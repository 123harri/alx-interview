#!/usr/bin/python3
"""
0-lockboxes module

This module provides the canUnlockAll function to
determine if all boxes
can be unlocked given a list of boxes with keys.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list of lists): A list of boxes,
        each containing a list of keys.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = [0]

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    return all(unlocked)
