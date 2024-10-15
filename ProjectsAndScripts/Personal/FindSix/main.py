#!/usr/bin/env python

from random import randint


def fill_matrix(
    x: int = 70, y: int = 20,
    fill_with: int = 5, find_for: int = 6
) -> str:
  """ Returns matrix and index for `find_for` """
  matrix = [f"{fill_with}" * x] * y
  by_x = randint(0, x-1)
  by_y = randint(0, y-1)
  target = list(matrix[by_y])
  target[by_x] = f"{find_for}"
  matrix[by_y] = ''.join(target)
  return '\n'.join(matrix)


def show_matrix(matrix: str, fill_with: int, find_for: int):
    print(matrix)
    input('- Click `Enter` to highlight the target\n')
    for fixed in (
        f"{fill_with}{find_for}{fill_with}",
        f"{fill_with}{fill_with}{find_for}",
        f"{find_for}{fill_with}{fill_with}"
    ):
      if matrix.find(fixed) != -1:
        print(matrix.replace(fixed, f"[{find_for}]"))
        break


def main():
  fill_with = 5
  find_for = 6
  while True:
    matrix = fill_matrix(fill_with=fill_with, find_for=find_for)
    show_matrix(matrix, fill_with, find_for)
    b = input('- Type `y` to break: ')
    if b.strip() == 'y':
      break



if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    pass
