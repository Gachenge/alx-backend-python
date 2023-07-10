#!/usr/bin/env python3
"""
Import wait_random from the previous python file that you’ve written
write an async routine called wait_n that takes in 2 int arguments
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List:
    """spawn wait_random n times with the specified max_delay"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    completed = await asyncio.gather(*tasks)
    delay = [task for task in completed]
    return delay
