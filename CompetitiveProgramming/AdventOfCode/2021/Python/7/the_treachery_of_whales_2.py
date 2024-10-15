#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  input_file = './input.txt'
  with open(input_file, 'r') as ftr:
    whales = list(map(int, ftr.read().strip().split(',')))
  sum_ = []
  # for k, i in enumerate(range(5, 6)):
  for k, i in enumerate(range(1, (len(whales)+1))):
    sum_.append(
      # XXX: https://www.youtube.com/watch?v=I_GB8DMGvVA&ab_channel=JonathanPaulson
      sum([(abs(x-i)*(abs(x-i)+1)/2) for x in whales])
    )
  print(min(sum_))
  # try: 199496249
  # try: 92948968

if __name__ == '__main__':
  main()
