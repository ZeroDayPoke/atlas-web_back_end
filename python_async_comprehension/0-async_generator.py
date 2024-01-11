#!/usr/bin/env python3
"""Task 0"""
import asyncio
import random


async def async_generator():
    """
    An asynchronous generator that yields 10 random numbers,
    each after waiting 1 second.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
