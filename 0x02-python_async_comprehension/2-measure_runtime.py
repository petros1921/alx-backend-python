#!/usr/bin/env python3
'''Task 2's module.
'''

import asyncio
import time
from .async_comprehension import async_comprehension

async def measure_runtime() -> float:
    '''Measures the runtime of executing async_comprehension four times in parallel.'''
    start_time = time.perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.perf_counter()

    return end_time - start_time