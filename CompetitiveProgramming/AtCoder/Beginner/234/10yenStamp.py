#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def main():
  start, stop = map(int, input().split(' '))
  if (start >= stop):
    return 0
  return math.ceil((stop - start) / 10)

if __name__ == '__main__':
  print(main())
