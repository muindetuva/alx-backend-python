#!/usr/bin/env python3
"""
Learning async
Function that returns number of seconds for a delay
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits a randome number of seconds (between 0 and max dealy) and returns.

    Parameters:
        max_delay (int): Max numbe of seconds to wait (default is 10)

    Returns:
        flaot: The actual number of secnds waited
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
