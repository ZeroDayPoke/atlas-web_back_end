#!/usr/bin/env python3
"""task 5"""


# ./5-sum_list.py
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floating-point numbers.

    Args:
    input_list (List[float]): A list of floating-point numbers.

    Returns:
    float: The sum of the numbers in the list.
    """
    return sum(input_list)
