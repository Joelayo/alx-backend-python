#!/usr/bin/env python3
'''import List and Union module'''
from typing import Callable

'''
Module for make_multiplier function
'''


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Creates a multiplier function.
    '''
    def multiply_by_multiplier(x: float) -> float:
        return multiplier * x
    return multiply_by_multiplier
