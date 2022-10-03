# pip install spacy
# python3 -m spacy download "en_core_web-sm"

import sys
import spacy
from collections import Counter


def load_target_data(file_name: str) -> str:
  with open(file_name) as ftr:
    return ftr.read()


def load_model() -> 'spacy.lang.en.English':
  return spacy.load("en_core_web_sm")


def clean_target(target: str) -> str:
  return target.replace('/', ' ')


def tokens_to_table(tokens: 'spacy.tokens.doc.Doc') -> str:
  table = """
  <table>
  """

  rows = """
    <tr>
      <td>{0}</td>
      <td style="text-align: right">{1}</td>
    </tr>
  """

  token_counter = Counter()

  for token in tokens:
    if ('NUM' in token.pos_) or ('PROPN' in token.pos_):
      token_counter.update((token.text,))

  for token, count in token_counter.items():
    table += rows.format(token, count)

  table += """
  </table>
  """

  return table


if __name__ == '__main__':
  target = sys.stdin.read()

  model = load_model()
  target = clean_target(target)
  tokens = model(target)
  table = tokens_to_table(tokens)
  sys.stdout.write(table)
