#!/usr/bin/env python3
"""3-tasks

Returning tasks
"""
import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns a wait_random task"""
    wait_random = __import__('0-basic_async_syntax').wait_random
    return asyncio.create_task(wait_random(max_delay))
