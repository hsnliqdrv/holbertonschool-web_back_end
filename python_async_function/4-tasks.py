#!/usr/bin/env python3
"""4-tasks

Returning tasks
"""
import asyncio


def task_wait_n(n: int, max_delay: int) -> asyncio.Task:
    """Returns a wait_n task"""
    wait_n = __import__('1-concurrent_coroutines').wait_n
    return asyncio.create_task(wait_n(n, max_delay))
