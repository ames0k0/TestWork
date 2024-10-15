#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  prev = None
  larger = 0
  with open('./input.txt', 'r') as ftr:
    for number in ftr.readlines():
      number = int(number.strip())
      if (prev is None):
        prev = number
        continue
      if (number > prev):
        larger += 1
      prev = number
  print(larger)

if __name__ == '__main__':
  main()
