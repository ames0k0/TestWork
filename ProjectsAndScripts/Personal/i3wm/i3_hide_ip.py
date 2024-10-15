#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳'

from sys import argv


def change_it(line):

    if argv[1] == 'on':
        return line.replace('# ', '')
    else:
        return f'# {line.lstrip()}'


def main():

    file = '/etc/i3status.conf'
    lines = (15, 16)

    with open(file, 'r') as fr:
        rded = fr.readlines()

    for line in lines:
        rded[line] = change_it(rded[line])

    with open(file, 'w') as fw:
        fw.write("".join(rded))


if __name__ == "__main__":
    main()
