#!/usr/bin/env python3
"""
This module defines an async function that uses an async comprehension
to collect values from an async generator.
"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random float values from an async generator
    using an asynchronous comprehension.

    Returns:
        List[float]: List of 10 random floats between 0 and 10
    """
    return [i async for i in async_generator()]
