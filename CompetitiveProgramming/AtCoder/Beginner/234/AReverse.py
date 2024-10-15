#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  start, stop = map(int, input().split(' '))
  string = input()
  s = ''
  m = ''
  e = ''
  for cidx, char in enumerate(string, 1):
    if (cidx < start):
      s += char
      continue
    if (cidx > stop):
      e += char
      continue
    m += char
  return (s + ''.join(reversed(m)) + e)

if __name__ == '__main__':
  print(main())
