#!/usr/bin/env python3
"""
This module provides a function to measure the average time
each wait_random coroutine takes when run concurrently via wait_n.
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time for running wait_n.

    Args:
        n (int): Number of coroutines to run
        max_delay (int): Maximum delay for each coroutine

    Returns:
        float: Average execution time per coroutine
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total_time = end - start
    return total_time / n
