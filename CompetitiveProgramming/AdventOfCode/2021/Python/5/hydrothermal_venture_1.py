#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

def find_larger(diagram):
  # x -> [(c, y), ...]
  cnts = {}
  for d in diagram:
    x, y = d
    fnd = cnts.get(x)
    if (fnd is None):
      cnts[x] = [(y, 1)]
    else:
      for i, (y1, c) in enumerate(fnd[:]):
        if ((y-1) == y1):
          cnts[x][i] = (y, c+1)
          break
      else:
        cnts[x].append((y, 1))
  m = None
  for v in cnts.values():
    for (y, c) in v:
      if (m is None):
        m = c
      elif (c > m):
        m = c
  print(cnts)
  # print(c)
  # print(max(cnts.values()))

def main():
  """
  (1..5)
  """
  diagram = []
  input_file = './input.txt'
  xy = get_max_diagram_coords(input_file)
  cntr = {}

  # try: 49
  # random: on    :)
  # try: 48
  # try: 50
  # random: off   :(

  with open(input_file, 'r') as ftr:
    for line in ftr.readlines():
      # 309,347 -> 309,464
      line = line.strip().split(' ')
      x1, y1 = map(int, line[0].split(','))
      x2, y2 = map(int, line[-1].split(','))
      if (x1 == x2):
        for y in range(y1, y2+1):
          # fnd = cntr.get(x1, 0)
          # cntr[x1] = fnd + 1
          diagram.append((x1, y))
      elif (y1 == y2):
        for x in range(x1, x2+1):
          diagram.append((x, y1))

  diagram = sorted(diagram, key=lambda x: x[1])
  find_larger(diagram)
  exit()
  print(diagram)
  # print(cntr)
  # print(max(cntr.values()))
  # print(diagram)

  # with open('./output_2.txt', 'w') as ftw:
  #   for d in diagram:
  #     ftw.write(''.join([str(i) for i in d])+'\n')

  # larger_points(diagram, xy)

# 0,9 -> 5,9

if __name__ == '__main__':
  main()
