#!/usr/bin/env python3
'''import Dict, Union, and TypeVar'''
from typing import Any, Mapping, Union, TypeVar

'''
Module for safely_get_value function
'''

T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    '''Retrieves a value from a dict using a given key.
    '''
    if key in dct:
        return dct[key]
    else:
        return default
