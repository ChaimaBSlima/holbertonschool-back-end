#!/usr/bin/env python3
''' 
chaima ben slima 
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' Return function that multiplies float by `multiplier`. '''
    return lambda x: x * multiplier

