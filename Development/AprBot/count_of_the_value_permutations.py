"""
0*7 -> 000_0000_1234567

BUG: duplicated permutations with zeros

+-------+---------+
| 0_7_0 |  value  |
+-------+---------+
| 0 1 2 | indexes | swapping `0` and `2` doesn't change the value
+-------+---------+
"""

def with_itertools(N: str) -> None:
  from itertools import permutations

  for idx, _ in enumerate(permutations(N, len(N)), start=1):
    pass

  print(idx)


def with_math(N: str) -> None:
  from math import factorial

  print(factorial(len(N)))


if __name__ == '__main__':
  import sys

  N = int(sys.argv[1]) # nocheck
  N = '0' * N + ''.join([str(i) for i in range(1, N+1)])

  # with_itertools(N)
  with_math(N)
