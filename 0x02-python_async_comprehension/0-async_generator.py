#!/usr/bin/env python3
"""
Async Generator
"""
from asyncio import sleep
from typing import Generator
from random import uniform


async def async_generator() -> Generator[float, None, None]:
    """
    Async Generator
    """
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
