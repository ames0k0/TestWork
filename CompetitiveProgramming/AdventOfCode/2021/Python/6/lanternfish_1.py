#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  input_file = './input_2.txt'
  with open(input_file, 'r') as ftr:
    fishes = list(map(int, ftr.read().strip().split(',')))
  for _ in range(80):
    for fidx, fish in enumerate(fishes[:]):
      if (fish == 0):
        fishes[fidx] = 6
        fishes.append(8)
      else:
        fishes[fidx] = (fish-1)
  print(len(fishes))

if __name__ == '__main__':
  main()
