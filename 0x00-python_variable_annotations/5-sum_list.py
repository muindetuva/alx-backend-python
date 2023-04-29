#!/usr/bin/env python3
'''
Module contains function that takes a list and sums its elements
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Takes a list of floats and returns the sum of all the elements

    Args:
        input_list (list): A list of floats.

    Returns:
        float: A sum of all the floats in the list
    '''

    sum: float = 0

    for n in input_list:
        sum = sum + n

    return sum
