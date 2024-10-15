#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  horizontal = 0
  depth = 0
  aim = 0
  with open('./input.txt', 'r') as ftr:
    for line in ftr.readlines():
      where, how_much = line.strip().split(' ')
      how_much = int(how_much)
      if (where == 'forward'):
        horizontal += how_much
        depth += (aim * how_much)
      elif (where == 'up'):
        aim -= how_much
      elif (where == 'down'):
        aim += how_much
  print(horizontal * depth)

if __name__ == '__main__':
  main()
