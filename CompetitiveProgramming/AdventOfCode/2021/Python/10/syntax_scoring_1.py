#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  input_file = './input.txt'
  scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
  }
  chars = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
  }
  u_chars = {v: k for k, v in chars.items()}
  s = 0
  with open(input_file, 'r') as ftr:
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
          s += scores.get(char)
          break

  print(s)

class Indexes:
  K=4 if (not True) else 3

if __name__ == '__main__':
  # main()
  i = Indexes()
  print(i.K)
