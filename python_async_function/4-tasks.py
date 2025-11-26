#!/usr/bin/env python3
"""4-tasks

Coroutines and concurrency
"""
import asyncio
import typing


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """Spawn wait_random n times and return delays in ascending order"""
    task_wait_random = __import__('3-tasks').task_wait_random
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = []
    for task in asyncio.as_completed(tasks):
        res = await task
        results.append(res)
    return results
