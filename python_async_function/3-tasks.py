#!/usr/bin/env python3
"""task 3"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task that executes wait_random
    with the specified max_delay.

    Args:
    max_delay (int): The maximum delay passed to wait_random.

    Returns:
    asyncio.Task: The created asyncio.Task object.
    """
    return asyncio.create_task(wait_random(max_delay))
