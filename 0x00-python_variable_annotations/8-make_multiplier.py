#!/usr/bin/env python3
"""Complex types - functions"""
from typing import List, Union, Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function make_multiplier that takes a float multiplier as
    argument and returns a function that multiplies a float by
    multiplier.
    """
    def func(k: float) -> float:
        """Multiplies multiplier"""
        return k * multiplier
    return func
