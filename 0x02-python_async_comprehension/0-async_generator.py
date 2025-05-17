#!/usr/bin/env python3
"""
This module defines an asynchronous generator that simulates
a data stream producing random float values over time.

The generator yields 10 random numbers between 0 and 10,
with a 1-second delay between each value.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously generate 10 random float values between 0 and 10.

    This coroutine simulates a stream of delayed data by:
    - Waiting for 1 second between values
    - Yielding a new random float each time

    Returns:
        AsyncGenerator[float, None]: async generator yielding 10 float values
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
