#!/usr/bin/env python3
'''import List and Tuple module'''
from typing import List, Tuple
'''
Module for combine_strings function
'''


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    '''Computes the length of a list of sequences.
    '''
    return [(i, len(i)) for i in lst]

