#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.

front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'
"""

from utils.args_to_r import validate


def main(string: str) -> str:
  return (string[:3] * 3)


tests = [
  (('Java',), 'JavJavJav'),
  (('Chocolate',), 'ChoChoCho'),
  (('abc',), 'abcabcabc')
]
validate(main, tests)
