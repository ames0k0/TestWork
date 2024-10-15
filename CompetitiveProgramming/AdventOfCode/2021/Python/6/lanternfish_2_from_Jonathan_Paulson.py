#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
No need to create a list of fishes and add new one to the end of the list
"""

from collections import defaultdict

def main():
  # XXX: COPY/PASTED
  input_file = './input.txt'
  X = defaultdict(int)
  with open(input_file, 'r') as ftr:
    for n in map(int, ftr.read().strip().split(',')):
      if (n not in X.keys()):
        X[n] = 0
      X[n] += 1
    for _ in range(256):
      Y = defaultdict(int)
      for x, cnt in X.items():
        # add new fish
        if (x == 0):
          Y[6] += cnt
          Y[8] += cnt
        else:
          Y[x-1] += cnt
      X = Y
    print(sum(X.values()))

if __name__ == '__main__':
  main()
