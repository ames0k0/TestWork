#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict

def main():
  input_file = './input.txt'
  scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
  }
  chars = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
  }
  u_chars = {v: k for k, v in chars.items()}
  lines = {}
  ld = []
  with open(input_file, 'r') as ftr:
    line_comp = defaultdict(str)
    for lidx, line in enumerate(ftr.readlines()):
      line = line.strip()
      stack = []
      for char in line:
        if (not stack):
          stack.append(char)
          continue
        start = chars.get(char)
        if (start is not None):
          stack.append(char)
          continue
        end = u_chars.get(char)
        if (stack[-1] == end):
          stack.pop(-1)
        else:
          if (lidx not in ld):
            ld.append(lidx)
          break
      if (stack) and (lidx not in ld):
        lines[lidx] = stack

  ls = defaultdict(int)
  for lidx, line in enumerate(lines.values()):
    lc = ''
    for char in reversed(line):
      lc += chars.get(char)
      ls[lidx] *= 5
      ls[lidx] += scores.get(lc[-1])

  vs = sorted(ls.values())
  print(vs[len(vs)//2])

if __name__ == '__main__':
  main()
