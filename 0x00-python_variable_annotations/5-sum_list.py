#!/usr/bin/env python3
"""
Complex types - list of floats
"""


def sum_list(input_list: list) -> float:
    """
    Function that takes a list input_list of floats as argument
    and returns their sum as a float.
    """
    total:
        float = 0
    for number in input_list:
        total += number
    return total
