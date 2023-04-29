#!/usr/bin/env python3
'''
Module contains function that returns a list of length of elememnts in a list
'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Returns a list of its elemtents and lengths

    Args:
        lst (List): A list

    Returns:
        List : A list of tuples
    '''
    return [(i, len(i)) for i in lst]
