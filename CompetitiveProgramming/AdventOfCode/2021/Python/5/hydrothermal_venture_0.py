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
          for r0, r1 in enumerate(diagram[ridx:]):
            if (r1[cidx] != '.'):
              diagram[ridx+r0][cidx] = '.'
              lc += 1
            else:
              if not lc:
                break
              larger[(ridx+r0, cidx)] = lc
              break
    else:
      break

  print(larger)

def main():
  input_file = './input_2.txt'
  xy = get_max_diagram_coords(input_file)
  diagram = create_diagram(xy, xy)
  with open(input_file, 'r') as ftr:
    for line in ftr.readlines():
      # 309,347 -> 309,464
      line = line.strip().split(' ')
      x1, y1 = map(int, line[0].split(','))
      x2, y2 = map(int, line[-1].split(','))
      if (x1 == x2):
        for y in range(y1, y2+1):
          prev_cover = diagram[y][x1]
          if (prev_cover == '.'):
            prev_cover = 1
          else:
            prev_cover += 1
          diagram[y][x1] = prev_cover
      elif (y1 == y2):
        for x in range(x1, x2+1):
          prev_cover = diagram[y1][x]
          if (prev_cover == '.'):
            prev_cover = 1
          else:
            prev_cover += 1
          diagram[y1][x] = prev_cover
      else:
        print('hhh', line)

  with open('./output_2.txt', 'w') as ftw:
    for d in diagram:
      ftw.write(''.join([str(i) for i in d])+'\n')

  larger_points(diagram, xy)

# 0,9 -> 5,9

if __name__ == '__main__':
  main()
