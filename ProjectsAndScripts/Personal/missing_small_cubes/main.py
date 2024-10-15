#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

"""
"""

x, y, z = 5, 4, 5
# ignored one
cube_count = (5*4)
filled_dimension = 2
array = np.zeros((y, x, z), dtype=np.int64)

index = 1

men = np.zeros((4, 5), dtype=np.int64)


for zet in array:
    if filled_dimension:
        filled_dimension -= 1
        continue

    not_filled = np.unique(zet[:-index, index:], return_counts=True)[1][0]
    cube_count += not_filled
    # array[:-zet, zet:] = not_filled
    men[:-index, index:] = not_filled
    index += 1


print(cube_count)
