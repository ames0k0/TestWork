#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict

def main():
  input_file = './input_2.txt'
  pairs = []
  with open(input_file, 'r') as ftr:
    prev_pair = None
    for line in ftr.readlines():
      line = line.strip().split(' ')
      if prev_pair is None:
        prev_pair = line[:-1]
      else:
        pairs.append((prev_pair, line))
        prev_pair = None

  cnts = {}
  for (ws, _) in pairs:
    for w in ws:
      unique = ''.join(sorted(list(w)))
      if (cnts.get(unique) is None):
        cnts[unique] = w

  cnt = 0
  us = cnts.values()
  print(len(cnts.keys()))
  # exit()
  for v in cnts.keys():
    for (_, us) in pairs:
      for u in us:
        # print((v == ''.join(sorted(list(u)))))
        if (v != ''.join(sorted(list(u)))):
          cnt += 1

  print(cnt)

  # try: 40

if __name__ == '__main__':
  main()
