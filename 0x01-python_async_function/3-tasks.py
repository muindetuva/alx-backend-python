#!/usr/bin/env python3
"""
This module defines a regular function that returns an asyncio.Task
wrapping the wait_random coroutine.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Return an asyncio.Task that wraps wait_random coroutine.

    Args:
        max_delay (int): Max delay to pass to wait_random

    Returns:
        asyncio.Task: A task that will run wait_random in the event loop
    """
    return asyncio.create_task(wait_random(max_delay))
