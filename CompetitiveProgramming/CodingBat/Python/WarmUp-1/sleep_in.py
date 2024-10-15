#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
"""

from utils.args_to_r import validate


def main(weekday: bool, vacation: bool) -> bool:
  if (not weekday) or vacation:
    return True
  return False


tests = [
  ((False, False), True),
  ((True, False), False),
  ((False, True), True)
]
validate(main, tests)
