#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳'

from re import findall #-----------#
from itertools import combinations #
from functools import reduce #-----#


def find_max_zeros(A):
    nem = [f"{reduce(lambda x, y: x*y, comb)}" for comb in combinations(A, 3)]
    return len(max(findall(r'0+', "".join(nem))))

A = [7, 15, 6, 20, 5, 10]
print(_ne(A))
