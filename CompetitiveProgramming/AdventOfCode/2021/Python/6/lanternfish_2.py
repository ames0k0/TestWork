#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  input_file = './input_2.txt'
  with open(input_file, 'r') as ftr:
    fishes = ftr.read().strip().replace(',', '')
  for _ in range(256):
    new_fishes = ''
    appended = ''
    for fish in fishes:
      if (fish == '0'):
        appended += '8'
        fish = '6'
      else:
        fish = str(int(fish)-1)
      new_fishes += fish
    fishes = (new_fishes + appended)
  # print(fishes)
  print(len(fishes))

if __name__ == '__main__':
  main()
