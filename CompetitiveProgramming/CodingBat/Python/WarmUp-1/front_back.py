#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a string, return a new string where the first and last chars have been exchanged.

front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
"""

from utils.args_to_r import validate


def main(string: str) -> str:
  if len(string) <= 1:
    return string

  front = string[-1]
  back = string[0]

  for char in string[1:-1]:
    front += char
  return (front + back)


tests = [
  (('code',), 'eodc'),
  (('a',), 'a'),
  (('ab',), 'ba')
]
validate(main, tests)
