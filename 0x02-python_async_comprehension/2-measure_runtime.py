#!/usr/bin/env python3
"""
This module defines a coroutine that measures how long it takes to run
async_comprehension 4 times in parallel using asyncio.gather().
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Run async_comprehension four times in parallel and measure total runtime.

    Returns:
        float: Total time taken to run all four comprehensions concurrently
    """
    start_time = time.perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.perf_counter()

    return end_time - start_time
