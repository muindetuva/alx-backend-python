#!/usr/bin/env python3
'''
Module contains function that returns a function for multyplying a float
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Returns a function that multiplies a float by a multiplier

    Args:
        multiplier (float): Function's multiplier

    Returns:
        func: Multiplier function
    '''

    # Define multiplier function
    def fn(a: float) -> float:
        '''Multiplier function

        Args:
            a (float): Number to be multiplied by multiplier

        Returns:
            float: Result of multiplier operation
        '''
        return a * multiplier

    return fn
