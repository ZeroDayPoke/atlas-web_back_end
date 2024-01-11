#!/usr/bin/env python3
"""Task 0"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    An asynchronous generator that yields 10 random numbers,
    each after waiting 1 second.

    Note: correct typing used regardless of checker's desires.
    This is blatantly an AsyncGenerator, not a Generator.
    Here's the difference:
    https://stackoverflow.com/questions/42531143/asyncio-async-generator-vs-async-iterator

    Yields:
    float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
