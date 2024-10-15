import string
import itertools

def input_to_int_array():
  return [int(i) for i in input().strip().split(' ')]

K, M = input_to_int_array()

lines = []

for _ in range(K):
  lines.append(input_to_int_array())

target_char = string.ascii_lowercase[:K]
target_perm = itertools.permutations(target_char, K)

# abcd
for perm in target_perm:
  for pidx, char in enumerate(perm):
    cidx = target_char.index(char)

    for p, c in enumerate(perm):
      if p == pidx:
        for line_char in lines[cidx]:
          pass
      for p, c in enumerate(perm):
        if p == pidx:
          continue
        S = ...

for ridx, line in enumerate(lines):
  pass