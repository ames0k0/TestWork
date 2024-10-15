#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given an int n, return True if it is within 10 of 100 or 200.
Note: abs(num) computes the absolute value of a number.

near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False
"""

from utils.args_to_r import validate


def main(n: int) -> bool:
  default = 10
  for d in (100, 200):
    dmin = (d - default)
    dmax = (d + default)
    if (n >= dmin) and (n <= dmax):
      return True
  return False


tests = [
  ((93,), True),
  ((90,), True),
  ((89,), False)
]
validate(main, tests)
