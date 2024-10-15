#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def print_lines(d):
  for i in range(10):
    for j in range(10):
      print(d[(i, j)], end='')
    print()

def main():
  input_file = './input_2.txt'
  # d[row, col] = 1
  d = {}
  u = []
  with open(input_file, 'r') as ftr:
    for lidx, line in enumerate(ftr.readlines()):
      for cidx, char in enumerate(line.strip()):
        d[(lidx, cidx)] = int(char)

    for n in range(2):
      print(f"\nSTEP_{n+1}")
      for (lidx, cidx), char in d.items():
        char += 1
        if (char >= 10):
          u.append((lidx, cidx))
          char = 0
        d[(lidx, cidx)] = char

      while u:
        for (n_lidx, n_cidx) in u[:]:
          for i in range(10):
            for j in range(10):
              if (i == n_lidx) or (j == n_cidx):
                char = d[(i, j)]
                char += 1
                if (char == 10):
                  u.append((i, j))
                  char = 0
                d[(i, j)] = char
          u.pop(0)
      print_lines(d)

if __name__ == '__main__':
  main()
