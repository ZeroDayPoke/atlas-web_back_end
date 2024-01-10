#!/usr/bin/env python3
"""task 2"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns the average time per call.

    Args:
    n (int): The number of times to spawn wait_random.
    max_delay (int): The maximum delay passed to wait_random.

    Returns:
    float: The average time per call.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total_time = end - start
    return total_time / n
