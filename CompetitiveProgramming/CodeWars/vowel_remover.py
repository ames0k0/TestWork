#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main(s):
  vowel = ('a', 'e', 'i', 'o', 'u')
  return ''.join([i for i in s if i not in vowel])


if __name__ == '__main__':
  main('')
