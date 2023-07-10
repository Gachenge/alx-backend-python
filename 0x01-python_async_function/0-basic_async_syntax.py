#!/usr/bin/env python3
"""
asynchronous coroutine that takes an integer argument(max_delay)
that waits for a random delay between 0 and max_delay
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """async function that waits for a random delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
