#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  input_file = './input.txt'
  with open(input_file, 'r') as ftr:
    whales = list(map(int, ftr.read().strip().split(',')))
  sum_ = []
  for i in range(1, (len(whales)+1)):
    sum_.append(
      sum([abs(x-i) for x in whales])
    )
  print(min(sum_))
  # try: 457056
  # try: 340052

if __name__ == '__main__':
  main()
