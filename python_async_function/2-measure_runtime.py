#!/usr/bin/env python3
"""2-measure_runtime

Measures total runtime
"""
import asyncio
import time


def measure_time(n: int, max_delay: int) -> float:
    """Measures runtime of wait_n"""
    wait_n = __import__('1-concurrent_coroutines').wait_n
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
