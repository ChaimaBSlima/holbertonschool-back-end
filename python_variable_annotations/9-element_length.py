#!/usr/bin/env python3
''' 
chaima ben slima 
'''

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Return list of tuples
    '''
    return [(i, len(i)) for i in lst]
