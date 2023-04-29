#!/usr/bin/env python3
'''
Module contains function that sums mixed floats and ints
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Sums a list of numbers

    Args:
        mxd_lst (list): A list of numbers

    Returns:
        float: A sum of all numbers in the list
    '''

    sum: float = 0

    for n in mxd_lst:
        sum = sum + n

    return sum
