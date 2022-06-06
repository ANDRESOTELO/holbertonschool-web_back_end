#!/usr/bin/env python3
"""
Complex types - list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Function that takes a list input_list of floats as argument
    and returns their sum as a float.
    """
    total = 0
    for number in input_list:
        total += number
    return total
