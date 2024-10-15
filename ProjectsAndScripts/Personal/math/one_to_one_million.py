#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳'

import numpy as np


def otom(number):
    """ src: https://www.youtube.com/watch?v=Dd81F6-Ar_0
    -----------------
    n: 5  | 1+2+3+4+5
    n: 10 | ...1+0
    """
    # one to one million
    r = 0
    for num in np.arange(1, number+1):
        # list(14) -> ['1', '4']
        r += np.sum(np.array(list('{}'.format(str(num)))).astype('int'))
    print(r)

#otom(1000000)
