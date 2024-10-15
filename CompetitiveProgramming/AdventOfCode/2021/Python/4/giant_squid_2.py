#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def check_win(r, c, board):
  row = board[r]
  if all(map(lambda x: x == '-', row)):
    return True
  col = [row[c] for row in board]
  if all(map(lambda x: x == '-', col)):
    return True
  return False

def sum_win(board, nb):
  not_changed = 0
  for row in board:
    for col in row:
      if (col != '-'):
        not_changed += int(col)
  return not_changed * int(nb)

def main():
  bingo = None
  bingo_limit = 0
  board = {}
  board_index = 0
  winner = {}
  winner_index = 0

  with open('./input.txt', 'r') as ftr:
    for lidx, line in enumerate(ftr.readlines()):
      line = line.strip()
      if (not lidx) and line:
        bingo = line.split(',')
        continue
      if (not line) and bingo:
        board_index += 1
        continue
      if (board.get(board_index) is None):
        board[board_index] = []
      board[board_index].append(list(filter(bool, line.split(' '))))

  while True:
    next_bingo = bingo[bingo_limit:bingo_limit+5]
    if (not next_bingo):
      break
    bingo_limit += 5

    # try: 390
    # try: 1666
    # try: 4590

    for nb in next_bingo:
      for k, iboard in board.copy().items():
        if (k in winner.keys()):
          continue
        for r, row in enumerate(iboard):
          for c, col in enumerate(row):
            if (col == nb):
              board[k][r][c] = '-'
              if check_win(r, c, board[k]):
                if (winner.get(k) is None):
                  winner[k] = {}
                winner[k][winner_index] = (sum_win(board[k], nb), nb)
                winner_index += 1

    if (len(winner.keys()) == len(board.keys())):
      for v in winner.values():
        if (v.get(winner_index-1) is not None):
          return v[winner_index-1][0]

if __name__ == '__main__':
  print(main())
