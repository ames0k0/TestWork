#!/usr/bin/env python3
# -*- coding: utf-8 -*-

first = input()
second = input().split(' ')
third = input()

int_sum = sum(map(lambda x: int(x), (first, *second)))

print(int_sum, third)
