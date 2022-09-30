#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# vim: ts=2, sw=2, expandtab

# TASK
# Напишите код, который извлекает из строки все слова, \
#   а затем выводит в порядке убывания частоты в этой строке только те, у которых частота >1.
# В строке могут быть слова на английском, знаки пунктуации, пробелы и урлы.
# Урл словом не является и должен быть отброшен.

# NOTES
# Частота - Как часто слово встречается в строке
# В этой строке - просто вывести в stdout

# TASK-features
# English words -> word
# Punctuation marks -> as a delimiter
# Spaces -> as a delimiter
# Urls -> not a word
# Print only words with a condition -> (word.count > 1)

import re
import typing
import string
import random
from collections import Counter


def split_by_urls(target: str) -> typing.List[str]:
  """Splitting by urls, so splitting by punctuations don't breaking the urls
  """
  # import urllib
  # urllib.parse.urlparse(target)

  # SEE: https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_URL
  # E.g: http(s)://(www.)google.com(:80)
  return re.split(
    r"http(?:s)?://(?:www.)?[\w+\.]+(?:\:\d+)?[\/\w+(-|+)?]+",
    target
  )


def split_by_punctuations(target: str) -> str:
  """Splitting by punctuations to get only words
  """
  # SEE: https://stackoverflow.com/a/13184791
  or_punctuation = '|'.join(
    map(re.escape, (string.whitespace[0] + string.punctuation))
  )
  return re.split(
    or_punctuation,
    target
  )


def filter_by_count(target: typing.Tuple[str]) -> typing.List[str]:
  most_common_only = []
  for (word, count) in Counter(target).most_common():
    if (count <= 1):
      break
    # Цифры != Слова ?
    if (word.isdigit()):
      continue
    most_common_only.append(word)

    # XXX: one line
    # print(word, end='\n')
  # print()

  # XXX: for test()
  return most_common_only


def random_numbers(limit: int = 50) -> typing.List[int]:
  return [random.randint(1, 10) for n in range(limit)]


def main(target: str) -> str:
  # A -> a
  target = target.strip().lower()

  if (not target):
    return target

  without_urls = split_by_urls(target)
  clean_target = ' '.join(
    [subs for subs in filter(str.strip, without_urls)]
  )

  without_punctuation = split_by_punctuations(clean_target)
  clean_target = tuple(filter(bool, without_punctuation))

  most_common_words = ' '.join(filter_by_count(clean_target))

  # import sys
  # sys.stdout.write(most_common_words)
  print(most_common_words)

  return most_common_words


def test() -> typing.Optional[AssertionError]:
  tests = [
    (
      "http://a.b:44 fkejjijoe http://t.me fef http://w.com http://j.fje.ocm https://developer.mozilla.org",
      ''
    ),
    (
      "Please visit my web-site: it's https://google.com/visit",
      ''
    ),
    (
      "a aa b bb+bb c_c-c+c a*4*6 dd&;4",
      'c a bb'
    ),
    (
      'А можно ли говорить: крайний раз, крайний день, крайний, крайний, крайний…',
      'крайний'
    ),
    (
      r'\alpha, \Alpha, \beta, \Beta, \gamma, \Gamma, \pi, \Pi, \phi, \varphi, \mu, \Phi, \varPhi',
      'alpha beta gamma pi phi varphi'
    ),
    (
      # random_numbers
      '8, 10, 9, 10, 6, 5, 9, 10, 1, 2, 4, 8, 7, 3, 2, 4, 8, 9, 10, 1, 2, 4, 9, 7, 2, 6, 7, 1, 10, 5, 4, 2, 1, 8, 1, 6, 10, 5, 10, 2, 6, 7, 10, 7, 1, 4, 9, 7, 2, 1',
      ''
    ),
    (
      '',
      ''
    )
  ]
  for (target, result) in tests:
    assert main(target) == result


if __name__ == '__main__':
  test()
