#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  binary_data = {}
  gamma = ''
  epsilon = ''
  with open('./input.txt', 'r') as ftr:
    for line in ftr.readlines():
      for cidx, char in enumerate(line.strip()):
        if (binary_data.get(cidx) is None):
          binary_data[cidx] = {'0': 0, '1': 0}
        binary_data[cidx][char] += 1

  binary_length = max(binary_data.keys())
  for i in range(binary_length+1):
    if (binary_data[i]['0'] > binary_data[i]['1']):
      gamma += '0'
      epsilon += '1'
    else:
      gamma += '1'
      epsilon += '0'
  gamma, epsilon = map(lambda x: int(x, 2), (gamma, epsilon))
  print(gamma * epsilon)

if __name__ == '__main__':
  main()
