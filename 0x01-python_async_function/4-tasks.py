#!/usr/bin/env python3
"""
Import wait_random from the previous python file that you’ve written
write an async routine called wait_n that takes in 2 int arguments
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List:
    """calls task_wait_random"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    completed = await asyncio.gather(*tasks)
    delays = sorted(completed)
    return delays
