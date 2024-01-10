#!/usr/bin/env python3
"""task 0"""


# ./0-basic_async_syntax.py
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay.

    Args:
    max_delay (int): The maximum delay time in seconds. Default is 10.

    Returns:
    float: The actual delay time.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
