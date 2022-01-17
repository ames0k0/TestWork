#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Тестовое заданьице imot.io

vim: ts=2, et
"""

from typing import NewType, Union, List, Dict


STT_RES_TYPE = NewType('STT_RES_TYPE', List[Dict[str, Union[int, float]]])
STT_FIX_TYPE = NewType('STT_FIX_TYPE', Dict[str, str])


def fix_function(stt_res: STT_RES_TYPE, stt_rules: STT_FIX_TYPE) -> STT_RES_TYPE:
  """Fixing the STT-Engine result

  Parameters
  ----------
  stt_res : list of dict
    recognized words by STT-Engine
  stt_rules : dict
    real words

  Returns
  -------
  list of dict
    fixed *stt_res
  """
  fixed_stt_res = []
  stt_rules_pieces = [k.split(' ') for k in stt_rules.keys()]
  skip_data = 0

  for didx, data in enumerate(stt_res):
    if skip_data:
      skip_data -= 1
      continue
    for pieces in stt_rules_pieces:
      plen = len(pieces)
      if pieces[0] == data['word']:
        if plen == 1:
          data['word'] = stt_rules.get(' '.join(pieces))
          fixed_stt_res.append(data)
          break
        for nidx, ndata in enumerate(stt_res[(didx+1):], start=1):
          if nidx == plen:
            break
          if ndata['word'] != pieces[nidx]:
            break
          if nidx == (plen-1):
            data.update(
              {
                'word': stt_rules.get(' '.join(pieces)),
                'end': ndata['end']
              }
            )
            skip_data = (plen-1)
            break
    else:
      fixed_stt_res.append(data)

  return fixed_stt_res


def main():
  """Entrypoint, used as a unittest
  """
  STT_RES = [
    {"word": "добрый", "start": 0.5, "end": 0.7},
    {"word": "день", "start": 0.8, "end": 1.0},
    {"word": "зайка", "start": 1.1, "end": 1.3},
    {"word": "телеком", "start": 1.35, "end": 1.8},
    {"word": "оператор", "start": 1.9, "end": 2.3},
    {"word": "вася", "start": 2.35, "end": 2.6},
    {"word": "чем", "start": 2.8, "end": 3},
    {"word": "могу", "start": 3.1, "end": 3.2},
    {"word": "помочь", "start": 3.3, "end": 3.5},
  ]
  FIX_RULES = {
    "матрешка": "смотрешка",
    "зайка телеком": "экотелеком",
    "как целиком": "экотелеком",
    "это от матери": "это мастер",
  }
  STT_RES_FIXED = [
    {"word": "добрый", "start": 0.5, "end": 0.7},
    {"word": "день", "start": 0.8, "end": 1.0},
    {"word": "экотелеком", "start": 1.1, "end": 1.8},
    {"word": "оператор", "start": 1.9, "end": 2.3},
    {"word": "вася", "start": 2.35, "end": 2.6},
    {"word": "чем", "start": 2.8, "end": 3},
    {"word": "могу", "start": 3.1, "end": 3.2},
    {"word": "помочь", "start": 3.3, "end": 3.5},
  ]
  assert fix_function(STT_RES, FIX_RULES) == STT_RES_FIXED, \
    '"multiple word" index in the middle'

  TEST_RES = [
    {"word": "могу", "start": 3.1, "end": 3.2},
    {"word": "помочь", "start": 3.3, "end": 3.5},
  ]
  TEST_RULES = FIX_RULES.copy()
  TEST_RULES['могу помочь'] = 'foo'
  TEST_FIXED = [
    {"word": "foo", "start": 3.1, "end": 3.5},
  ]
  assert fix_function(TEST_RES, TEST_RULES) == TEST_FIXED, \
    '"multiple word" index at the end'

  TEST_RES = [
    {"word": "foo", "start": 3.1, "end": 3.2},
    {"word": "bar", "start": 3.3, "end": 3.5},
    {"word": "a", "start": 3.7, "end": 3.9},
  ]
  TEST_RULES = {'a': 'baz'}
  TEST_FIXED = [
    {"word": "foo", "start": 3.1, "end": 3.2},
    {"word": "bar", "start": 3.3, "end": 3.5},
    {"word": "baz", "start": 3.7, "end": 3.9},
  ]
  assert fix_function(TEST_RES, TEST_RULES) == TEST_FIXED, \
    '"single word" index at the end'

  TEST_RES = [
    {"word": "foo", "start": 3.1, "end": 3.2},
    {"word": "bar", "start": 3.3, "end": 3.5},
    {"word": "baz", "start": 3.7, "end": 3.9},
  ]
  TEST_RULES = {'foo bar a': 'baz'}
  TEST_FIXED = [
    {"word": "foo", "start": 3.1, "end": 3.2},
    {"word": "bar", "start": 3.3, "end": 3.5},
    {"word": "baz", "start": 3.7, "end": 3.9},
  ]
  assert fix_function(TEST_RES, TEST_RULES) == TEST_FIXED, \
    'broken "multiple word"'


if __name__ == '__main__':
  main()
