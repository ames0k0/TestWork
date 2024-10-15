#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given 2 int values, return True if one is negative and one is positive.
Except if the parameter "negative" is True, then return True only if both are negative.

pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True
"""

from utils.args_to_r import validate


def main(a: int, b: int, negative: bool) -> bool:
  if negative and ((a < 0) and (b < 0)):
    return True
  if (a < 0) or (b < 0):
    if ((a > 0) or (b > 0)):
      return True if (not negative) else False
  return False


tests = [
  ((1, -1, False), True),
  ((-1, 1, False), True),
  ((-4, -5, True), True)
]
validate(main, tests)
