#!/usr/bin/env python3
"""
This module provides a coroutine wait_n that concurrently runs wait_random
multiple times and returns the list of delays in order of completion.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run wait_random n times concurrently and return the list of delays
    in the order they complete.

    Parameters:
        n (int): Number of times to run wait_random
        max_delay (int): Maximum delay value passed to wait_random

    Returns:
        List[float]: Delays returned, ordered by completion time
    """

    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []

    for completed in asyncio.as_completed(tasks):
        result = await completed
        delays.append(result)

    return delays
