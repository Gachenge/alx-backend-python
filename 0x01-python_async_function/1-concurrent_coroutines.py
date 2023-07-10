#!/usr/bin/env python3
"""
Import wait_random from the previous python file that youve written
write an async routine called wait_n that takes in 2 int arguments
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List:
    """spawn wait_random n times with the specified max_delay"""
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
