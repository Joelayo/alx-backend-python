#!/usr/bin/env python3
'''Task 0's module.
'''
import asyncio
import random


async def async_generator():
    '''Generates a sequence of 10 numbers.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield round(random.uniform(0, 10), 10)
