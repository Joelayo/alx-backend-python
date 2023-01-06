#!/usr/bin/env python3
'''import List,Iterable, Sequence, and Tuple module'''
from typing import Iterable, Sequence, Tuple, List

'''
Module for combine_strings function
'''


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Computes the length of a list of sequences.
    '''
    return [(i, len(i)) for i in lst]
