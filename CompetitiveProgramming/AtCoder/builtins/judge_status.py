#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import sqlite3
from typing import Union, List, Callable
from collections.abc import Iterable

import pandas as pd
import numpy as np


"""
Requirements
------------
lxml==4.6.3
numpy==1.21.2
pandas==1.3.2
python-dateutil==2.8.2
pytz==2021.1
six==1.16.0
"""


STATIC_FOLDER = 'static'
DATABASE = os.path.join(STATIC_FOLDER, 'atcoder.bak')
TABLE_NAME = 'judge_status'


def read_from_database(curr: sqlite3.Cursor) -> None:
  curr.execute(f"SELECT * FROM {TABLE_NAME}")
  data = curr.fetchall()

  if (not status):
    return print_explanation(data, filter_function=lambda x: True)

  return print_explanation(data)


def clean_string(target: Iterable[str]) -> List[str]:
  return [t.strip() for t in target]


def create_database_table(curr: sqlite3.Cursor) -> None:
  curr.execute(
    f"""
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
      status VARCHAR(3),
      explanation TEXT
    )
    """
  )


def store_judge_status(curr: sqlite3.Cursor, conn: sqlite3.Connection, df: pd.DataFrame) -> None:
  create_database_table(curr)

  df.apply(clean_string)

  curr.executemany(
    f"INSERT INTO {TABLE_NAME} VALUES (?, ?)", df.values
  )
  conn.commit()


def print_explanation(data: Union[np.ndarray, List[str]], *,
                      filter_function: Callable = lambda x: (x == status)) -> None:
  for (s, e) in data:
    if filter_function(s):
      print(f"{s:<3} > {e}")


def read_from_web(curr: sqlite3.Cursor, conn: sqlite3.Connection) -> None:
  judge_status_url = 'https://atcoder.jp/contests/practice'

  df = pd.read_html(judge_status_url)[0]
  store_judge_status(curr, conn, df)

  print_explanation(df.values, filter_function=lambda x: True)


def main():
  with sqlite3.connect(DATABASE) as conn:
    curr = conn.cursor()

    if (os.path.getsize(DATABASE)):
      return read_from_database(curr)

    return read_from_web(curr, conn)


if __name__ == '__main__':
  status = ''

  if (len(sys.argv) > 1):
    status = clean_string(sys.argv[1:])[0]

  main()
