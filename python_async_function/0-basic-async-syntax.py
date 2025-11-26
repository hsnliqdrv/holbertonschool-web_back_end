#!/usr/bin/env python3
"""0-basic_async_syntax

Basic Async Syntax
"""
import random, asyncio


async def wait_random(max_delay=10):
    """Wait for a random length of time and return"""
    time = random.uniform(0, max_delay)
    await asyncio.sleep(time)
    return time
