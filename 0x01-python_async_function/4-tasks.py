#!/usr/bin/env python3
"""
This module defines task_wait_n which runs multiple wait_random tasks
concurrently.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run task_wait_random n times and return the delays in order of completion.

    Args:
        n (int): Number of tasks to run
        max_delay (int): Max delay for each task

    Returns:
        List[float]: Delays returned by each task, in order of completion
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for completed in asyncio.as_completed(tasks):
        result = await completed
        delays.append(result)

    return delays
