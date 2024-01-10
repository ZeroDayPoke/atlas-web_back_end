#!/usr/bin/env python3
"""task 1"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay and returns the delays
    in ascending order based on completion order.

    Args:
    n (int): The number of times to spawn wait_random.
    max_delay (int): The maximum delay passed to wait_random.

    Returns:
    List[float]: A list of delays from each wait_random call in ascending order based on completion.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    completed_delays = []
    while tasks:
        done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        for task in done:
            completed_delays.append(task.result())
            tasks.remove(task)
    return completed_delays
