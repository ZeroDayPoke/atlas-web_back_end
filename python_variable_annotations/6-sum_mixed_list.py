#!/usr/bin/env python3
"""task 6"""


# ./6-sum_mixed_list.py
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list containing both integers and floats.

    Args:
    mxd_lst (List[Union[int, float]]): A list containing integers and floats.

    Returns:
    float: The sum of the numbers in the list.
    """
    return sum(mxd_lst)
