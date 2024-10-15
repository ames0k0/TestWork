#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#!/bin/python3

import math
import os
import random
import re
import sys


def arr_sum(arr: list, row_start: int, col_start: int) -> int:
    sum_ = 0

    for ridx, row in enumerate(arr[row_start:row_start+3]):
        # for col in row[col_start:col_start+3]:
        if ridx == 1:
            sum_ += row[col_start+1]
        else:
            sum_ += sum(row[col_start:col_start+3])

    return sum_


def solve(arr):
    """
    arr[h] :: len(arr[h]) == 2
    arr[v] :: len(arr[v]) == 3
    """
    arr_sums = []

    for i in (0, 1, 2, 3):
        for j in (0, 1, 2, 3):
            arr_sums.append(arr_sum(arr, i, j))

    print(max(arr_sums))



if __name__ == '__main__':
    arr = []

    kk = (
    '1 1 1 0 0 0',
    '0 1 0 0 0 0',
    '1 1 1 0 0 0',
    '0 0 2 4 4 0',
    '0 0 0 2 0 0',
    '0 0 1 2 4 0'
    )

    for each in kk:
        arr.append(list(map(lambda x: int(x), each.split())))

    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))

    solve(arr)
