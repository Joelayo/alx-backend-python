#!/usr/bin/env python3
'''import Any, Union, Sequence, and None module'''
from typing import Any, Sequence, Union, None

'''
Module for safe_first_element function
'''


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Compute the first element of a given sequence'''
    if lst:
        return lst[0]
    else:
        return None
