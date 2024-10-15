#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳'

from os import chdir

"""
tor-browser_en-US/
    Browser/ *
    start-tor-browser.desktop
    tor_start_as_root.py
"""

def main():
    new = []
    nam = 'start-tor-browser'
    chdir('Browser')

    with open(nam, 'r') as f:
        for line in f.readlines():
            if '`id -u`' in line:
                new.append(line.replace('0', '1'))
            else:
                new.append(line)

    with open(nam, 'w') as f:
        f.write("".join(new))


if __name__ == "__main__":
    main()
