#!/usr/bin/env python3
"""0-basic_async_syntax

Basic Async Syntax
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random length of time and return"""
    time = random.uniform(0, max_delay)
    await asyncio.sleep(time)
    return time
