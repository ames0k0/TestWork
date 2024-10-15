#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

makes10(9, 10) → True
makes10(9, 9) → False
makes10(1, 9) → True
"""

from utils.args_to_r import validate


def main(a: int, b: int) -> bool:
  default = 10
  if (a == default) or (b == default):
    return True
  s = (a + b)
  if (s == default):
    return True
  return False

tests = [
  ((9, 10), True),
  ((9, 9), False),
  ((1, 9), True)
]
validate(main, tests)
