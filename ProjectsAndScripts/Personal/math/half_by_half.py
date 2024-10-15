#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳'


def hbh(a, b, mt=1, l=1):
    """
    a = half a + half b:: a/2+b/2 * mt
    b = half b + half a:: b/2+a/2 * mt

    ARGS:   a  - first  number
            b  - second number
            mt - multiplication to
            l  - loop
    """
    for _ in range(l):
        try:
            a, b = (b/2)*mt, (a/2)*mt   # ERROR:  **
        except OverflowError:
            print('Numberical result out of range')
            return False                # STOP SCRIPT HERE
    return a, b

print(hbh(2, 4, 4, 8))
