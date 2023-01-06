#!/usr/bin/env python3
from typing import List
'''
Module for declared variable
'''


def sum_list(input_list: List[float]) -> float:
    '''Returns input_list sum as a float'''
    sum = 0.0
    for i in input_list:
        sum += i
    return sum
