#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given an int n, return the absolute difference between n and 21, \
  except return double the absolute difference if n is over 21.

diff21(19) → 2
diff21(10) → 11
diff21(21) → 0
"""

from utils.args_to_r import validate


def main(n: int) -> int:
  default = 21
  return (default - n) if (n < default) else ((n - default) * 2)


tests = [
  ((19,), 2),
  ((10,), 11),
  ((21,), 0),
  # for doubling
  ((30,), 18)
]
validate(main, tests)
