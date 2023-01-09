#!/usr/bin/env python3
''' Import Asyncio and Random '''
import asyncio
import random

''' Module for wait_random function '''


async def wait_random(max_delay: int = 10) -> float:
    ''' Waits for a random number of seconds'''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
