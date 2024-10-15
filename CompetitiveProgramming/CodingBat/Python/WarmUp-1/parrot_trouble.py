#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
We have a loud talking parrot.
The "hour" parameter is the current hour time in the range 0..23.
We are in trouble if the parrot is talking and the hour is before 7 or after 20.
Return True if we are in trouble.

parrot_trouble(True, 6) → True
parrot_trouble(True, 7) → False
parrot_trouble(False, 6) → False
"""

from utils.args_to_r import validate


def main(talking: bool, hour: int) -> bool:
  if (hour < 7) or (hour > 20):
    if talking:
      return True
  return False


tests = [
  ((True, 6), True),
  ((True, 7), False),
  ((False, 6), False)
]
validate(main, tests)
