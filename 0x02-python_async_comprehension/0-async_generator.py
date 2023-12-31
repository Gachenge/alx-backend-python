#!/usr/bin/env python3
"""
coroutine that takes no arguments, loops 10 times and waits ! second
before yielding a random number
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """generate random numbers from 0 to 10"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
