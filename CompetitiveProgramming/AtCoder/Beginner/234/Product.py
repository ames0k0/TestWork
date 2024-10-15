#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from functools import lru_cache

@lru_cache
def calc(a, b):
  return (a * b)

def main():
  lines, target = map(int, input().split(' '))
  D = []
  for _ in range(lines):
    D.append(list(map(int, input().split(' '))))
  cnt = 0
  while D:
    MUL = None
    print('\n', D)
    for lidx, line in enumerate(D[:]):
      if not line:
        D.pop(lidx)
        continue
      for elem in line[:]:
        if (MUL is None):
          MUL = elem
          line.pop(0)
          continue
        print(MUL, '>>', elem)
        if (calc(MUL, elem) == target):
          cnt += 1
    time.sleep(2)
  print(cnt)

if __name__ == '__main__':
  main()
