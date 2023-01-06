#!/usr/bin/env python3
'''import List and Union module'''
from typing import Union, Tuple

'''
Module for to_kv function
'''


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Converts a key and its value to a tuple of the key and
    the square of its value.
    '''
    squared_v = v**2
    return (k, squared_v)
