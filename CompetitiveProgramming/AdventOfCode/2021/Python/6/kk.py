#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio

async def update_count(counts):
  new_counts = []
  for cidx, count in enumerate(counts):
    if (count == 0):
      count = 6
      new_counts.append(8)
    else:
      count = (count-1)
    counts[cidx] = count
  return counts + new_counts

async def main():
  input_file = './input_2.txt'
  with open(input_file, 'r') as ftr:
    fishes = list(map(int, ftr.read().strip().split(',')))
  # XXX: DO NOT RUN WITH 256 - pc memory is dead
  # for _ in range(256):
  for _ in range(80):
    tasks = []
    chunk_size = 0
    chunk_limit = 50
    while True:
      next_chunk_size = (chunk_size+chunk_limit)
      tasks.append(
        asyncio.create_task(update_count(fishes[chunk_size:next_chunk_size]))
      )
      chunk_size = next_chunk_size
      if (chunk_size > len(fishes)):
        break
    hello = await asyncio.gather(*tasks)
    fishes = []
    for h in hello:
      fishes.extend(h)

  print(len(fishes))

if __name__ == '__main__':
  asyncio.run(main())
