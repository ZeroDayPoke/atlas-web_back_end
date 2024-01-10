#!/usr/bin/env python3
"""task 8"""


# ./8-make_multiplier.py
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies its input by a specified multiplier.

    Args:
    multiplier (float): The multiplier value.

    Returns:
    Callable[[float], float]: A function that takes a float and returns
                              the result of multiplying it by the multiplier.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
