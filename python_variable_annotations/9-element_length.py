#!/usr/bin/env python3
"""task 9"""


# ./9-element_length.py
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, each containing an element
    from the input list and its length.

    Args:
    lst (Iterable[Sequence]): An iterable of sequences.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples where each tuple
                                contains a sequence from
                                lst and the length of that sequence.
    """
    return [(i, len(i)) for i in lst]
