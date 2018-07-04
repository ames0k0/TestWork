#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳'

from itertools import combinations
from functools import reduce
from re import findall


def ne(A):
    nem = []
    cbs = combinations(A, 3)
    for i in cbs:
        cm = reduce(lambda x, y: x*y, i)
        nem.append(f"{cm}")
    mx = "".join(nem)
    mg = findall(r'0+', mx)
    return len(max(mg))


A = [7, 15, 6, 20, 5, 10]
print(ne(A))
