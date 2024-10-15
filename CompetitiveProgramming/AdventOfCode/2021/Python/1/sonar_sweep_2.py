#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  prev = None
  larger = 0
  loaded_depth = []
  with open('./input.txt', 'r') as ftr:
    loaded = 0
    for number in ftr.readlines():
      number = int(number.strip())
      if (len(loaded_depth) != 3):
        loaded_depth.append(number)
      # 2+1
      if (len(loaded_depth) != 3):
        continue
      number = sum(loaded_depth)
      loaded_depth.pop(0)
      if (prev is None):
        prev = number
        continue
      if (number > prev):
        larger += 1
      prev = number
    print(larger)

if __name__ == '__main__':
  main()
