#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a non-empty string and an int n, return a new string where the char at index n has been removed.
The value of n will be a valid index of a char in the original string \
  (i.e. n will be in the range 0..len(str)-1 inclusive).

missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'
"""

from utils.args_to_r import validate


def main(string: str, n: int) -> str:
  new_string = ''
  for i, char in enumerate(string):
    if i != n:
      new_string += char
  return new_string


tests = [
  (('kitten', 1), 'ktten'),
  (('kitten', 0), 'itten'),
  (('kitten', 4), 'kittn')
]
validate(main, tests)
