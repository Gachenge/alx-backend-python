#!/usr/bin/env python3
"""
measure time function with integers n and max_delay measure
total execution time for wait_n
"""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure execution time"""
    time_now = time.time()
    asyncio.run(wait_n(n, max_delay))
    time_end = time.time()
    total_time = time_end - time_now
    return (total_time/n)
