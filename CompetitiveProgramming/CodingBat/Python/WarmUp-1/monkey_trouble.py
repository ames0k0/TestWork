#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.

monkey_trouble(True, True) → True
monkey_trouble(False, False) → True
monkey_trouble(True, False) → False
"""

from utils.args_to_r import validate


def main(a_smile: bool, b_smile: bool) -> bool:
  if (a_smile and b_smile):
    return True
  if (a_smile or b_smile):
    return False
  return True


tests = [
  ((True, True), True),
  ((False, False), True),
  ((True, False), False)
]
validate(main, tests)
