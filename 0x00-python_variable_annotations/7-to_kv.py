#!/usr/bin/env python3
'''
Module contains function that returns a tuple
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Function that takes a string and float or int and returns and tuple

    Args:
        k (string): First argument
        v (float | int): Second argument

    Returns:
        tuple: Contains all passed arguments
    '''
    return (k, v**2)
