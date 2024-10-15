#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a string, return a new string where "not " has been added to the front.
However, if the string already begins with "not", return the string unchanged.

not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
"""

from utils.args_to_r import validate


def main(string: str) -> str:
  default = 'not'
  if string.startswith(default):
    return string
  return (default + ' ' + string)


tests = [
  (('candy',), 'not candy'),
  (('x',), 'not x'),
  (('not bad',), 'not bad'),
]
validate(main, tests)
