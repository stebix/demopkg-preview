"""
This file contains some basic mock functions for the Pytorial.

@author: Jannik Stebani
"""
from itertools import repeat

def returns_ones(num: int) -> list[int]:
    """
    Returns a list of ones.

    Returns
    -------
    list[int]
        A list containing ones.
    """
    return list(repeat(1, num))