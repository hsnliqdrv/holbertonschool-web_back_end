#!/usr/bin/env python3
"""1-concurrent_coroutines

Coroutines and concurrency
"""
import asyncio
import typing


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """Spawn wait_random n times and return delays in ascending order"""
    wait_random = __import__('0-basic_async_syntax').wait_random
    coros = [wait_random(max_delay) for _ in range(n)]
    results = []
    for coro in asyncio.as_completed(coros):
        res = await coro
        results.append(res)
    return results
