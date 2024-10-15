#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  horizontal = 0
  depth = 0
  with open('./input.txt', 'r') as ftr:
    for line in ftr.readlines():
      where, how_much = line.strip().split(' ')
      how_much = int(how_much)
      if (where == 'forward'):
        horizontal += how_much
      elif (where == 'up'):
        depth -= how_much
      elif (where == 'down'):
        depth += how_much
  print(horizontal * depth)

if __name__ == '__main__':
  main()
