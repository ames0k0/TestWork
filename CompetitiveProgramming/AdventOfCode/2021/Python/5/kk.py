#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def create_diagram(x=10, y=10):
  diagram = [['.' for _ in range(y)] for _ in range(x)]
  return diagram

def get_max_diagram_coords(input_file):
  max_ = 0
  with open(input_file, 'r') as ftr:
    for line in ftr.readlines():
      # 309,347 -> 309,464
      line = line.strip().split(' ')
      x1, y1 = map(int, line[0].split(','))
      x2, y2 = map(int, line[-1].split(','))
      max_ = max(max_, x1, y1, x2, y2)
  return max_ + 1

def larger_points(diagram, y=10):
  larger = {}
  prev_row = 0
  prev_col = 0
  while True:
    for ridx, row in enumerate(diagram[:]):
      for cidx, col in enumerate(row):
        if (col != '.'):
          lc = 0
          uniq = []
          for r0, r1 in enumerate(diagram[ridx:]):
            h = r1[cidx]
            if (r1[cidx] != '.'):
              diagram[ridx+r0][cidx] = '.'
              lc += 1
              if (h not in uniq):
                uniq.append(h)
            else:
              if not lc:
                break
              larger[(ridx+r0, cidx)] = (lc, uniq)
              break
    else:
      break

  pc = None
  pv = None
  for k, (c, v) in larger.items():
    vl = len(v)
    if (vl == 1):
      continue
    if (pc is None) or (vl > pv):
      print(c, '->', v)
      pc = c
      pv = vl
    elif (vl == pv):
      if (c > pc):
        print(c, '->', v)
        pc = c
        pv = vl

  print(pc)
  # print(max(larger.values()))

def main():
  input_file = './input.txt'
  xy = get_max_diagram_coords(input_file)
  diagram = create_diagram(xy, xy)
  with open(input_file, 'r') as ftr:
    for line in ftr.readlines():
      # 309,347 -> 309,464
      line = line.strip().split(' ')
      x1, y1 = map(int, line[0].split(','))
      x2, y2 = map(int, line[-1].split(','))
      f = False
      if (x1 == x2) or (y1 == y2):
        f = True
      if (not f):
        continue
      if (y1 > y2):
        y1, y2 = y2, y1
      if (x1 > x2):
        x1, x2 = x2, x1

      # try: 897
      # try: 703
      # try: 603
      # try: 583

      for y in range(y1, y2+1):
        for x in range(x1, x2+1):
          prev_cover = diagram[y][x]
          if (prev_cover == '.'):
            prev_cover = 1
          else:
            prev_cover += 1
          diagram[y][x] = prev_cover

  with open('./output_2.txt', 'w') as ftw:
    for d in diagram:
      ftw.write(''.join([str(i) for i in d])+'\n')

  larger_points(diagram, xy)

# 0,9 -> 5,9

if __name__ == '__main__':
  main()
