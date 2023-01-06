#!/usr/bin/env python3
'''import List and Union module'''
from typing import List, Union

'''
Module for to_str function
'''


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''returns sum of mxd_lst of integers and floats as a float'''
    result = 0.0
    for item in mxd_lst:
        result += item
    return result
