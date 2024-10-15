#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  gamma = ''
  epsilon = ''
  data = []

  with open('./input.txt', 'r') as ftr:
    for line in ftr.readlines():
      data.append(line.strip())

  ndata = data[:]
  current_index = 0
  while True:
    o = []
    z = []
    for d in data:
      if (d[current_index] == '0'):
        o.append(d)
      else:
        z.append(d)
    if len(z) >= len(o):
      data = z
    else:
      data = o
    if (len(data) == 1):
      gamma = data[0]
      break
    current_index += 1

  current_index = 0
  data = ndata
  while True:
    o = []
    z = []
    for d in data:
      if (d[current_index] == '0'):
        o.append(d)
      else:
        z.append(d)
    if len(o) <= len(z):
      data = o
    else:
      data = z
    if (len(data) == 1):
      epsilon = data[0]
      break
    current_index += 1

  gamma, epsilon = map(lambda x: int(x, 2), (gamma, epsilon))
  print(gamma * epsilon)

if __name__ == '__main__':
  main()
  # try: 4623636
  # try: 10281312
  # try: 10388409
  # try: 1367118
  # try: 1794312
  # try: 236196
  # try: 1353024
