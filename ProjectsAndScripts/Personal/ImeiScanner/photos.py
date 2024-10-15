#!/usr/bin/env python
# -*- coding: utf-8 -*-

from json import loads
from os.path import dirname
from urllib.parse import urlparse, urlunparse
from urllib.parse import ParseResult
from urllib.request import urlopen


def main(photo_url: str, separator: str = '/'):
  url = urlparse(photo_url)
  url = ParseResult(url.scheme, url.netloc, dirname(url.path), '', '', '')
  response = urlopen(urlunparse(url))
  response_data = response.read()

  if not response_data:
    print('[!] No data')
    exit()

  response_data = loads(response_data)

  for item in response_data.get('items', []):
    url_path = separator.join((url.path, item.get('name', '')))
    photo_url = urlunparse(
      ParseResult(url.scheme, url.netloc, url_path, '', '', '')
    )

    # NOTE: It's not a photo
    # photo_url = 'https://firebasestorage.googleapis.com/v0/b/imei-scanner-d7ab3.appspot.com/o/profile_image/aPMfHgK9geXiq1URrhghqa5cjtV2'
    print(photo_url)


if __name__ == '__main__':
  photo_url = 'https://firebasestorage.googleapis.com/v0/b/imei-scanner-d7ab3.appspot.com/o/teahub.io-beautiful-wallpaper-hd-for-570952.jpg?alt=media&token=ad233afa-04bd-42f9-ac9b-5408e3387fe0'
  main(photo_url)
