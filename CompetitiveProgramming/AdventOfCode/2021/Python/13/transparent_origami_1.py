#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def transparent_y(coords, fold_y):
  up = []
  down = []
  for (x, y) in coords:
    if (y < fold_y):
      up.append((x, y))
    else:
      down.append((x, y))
  # sorted by y and reversed ?
  up = sorted(up, key=lambda x: x[1])
  down = sorted(down, key=lambda x: x[1])
  max_y = up[-1][1]
  for (x, y) in down:
    y = abs(y - max_y)
    if (not x) and (not y):
      continue
    up.append((x, y))
  return up

def transparent_x(coords, fold_x):
  left = []
  right = []
  for (x, y) in coords:
    if (x < fold_x):
      left.append((x, y))
    else:
      right.append((x, y))
  left = sorted(left, key=lambda x: x[0])
  right = sorted(right, key=lambda x: x[0])
  max_x = left[-1][0]
  for (x, y) in right:
    x = abs(x - max_x)
    if (not x) and (not y):
      continue
    left.append((x, y))
  return left

def main():
  input_file = './input.txt'
  # try: 983
  # try: 982
  coords = []
  fold_y = []
  fold_x = []
  first = False
  with open(input_file, 'r') as ftr:
    for line in ftr.readlines():
      line = line.strip()
      if ',' in line:
        coords.append(list(map(int, line.split(','))))
      if 'y' in line:
        coords = transparent_y(coords, int(line.split('=')[-1]))
        if (not first):
          first = True
          print(len(coords))
          exit()
      if 'x' in line:
        coords = transparent_x(coords, int(line.split('=')[-1]))
        print(line)
        if (not first):
          first = True
          print(len(coords))
          exit()

  # print(len(coords))

if __name__ == '__main__':
  main()
