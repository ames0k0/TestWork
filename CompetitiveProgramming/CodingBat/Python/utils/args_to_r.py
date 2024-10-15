#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List, Any, Callable


def validate(func: Callable, tests: List[Any]):
  for i, (args, r) in enumerate(tests):
    assert func(*args) == r, i
