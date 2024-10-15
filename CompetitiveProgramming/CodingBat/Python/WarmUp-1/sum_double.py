#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given two int values, return their sum. Unless the two values are the same, then return double their sum.

sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8
"""

from utils.args_to_r import validate


def main(a: int, b: int) -> int:
  s = (a + b)
  if (a == b):
    s *= 2
  return s


tests = [
  ((1, 2), 3),
  ((3, 2), 5),
  ((2, 2), 8),
]
validate(main, tests)
