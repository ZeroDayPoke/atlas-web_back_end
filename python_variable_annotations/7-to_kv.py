#!/usr/bin/env python3
"""task 7"""


# ./7-to_kv.py
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple containing a string and the square of a numeric value.

    Args:
    k (str): A string.
    v (Union[int, float]): An integer or float.

    Returns:
    Tuple[str, float]: A tuple where the first element is the string k,
                        and the second element is the square of v as a float.
    """
    return (k, float(v ** 2))
