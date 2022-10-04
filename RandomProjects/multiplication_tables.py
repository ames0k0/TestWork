#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳'

from argparse import ArgumentParser
from prettytable import PrettyTable


def _tlike(start, stop):
    res = []
    mino = len(str(start))
    for i in range(start, stop):
        if i >= 0 and i < 10:
            req = " " * (mino-1)
            res.append(req + str(i))
        else:
            res.append(i)
    return res


def _loop(head: list, sq: int, sp: bool) -> list:
    res = []
    mino = len(str(min(head)))
    for i in head:
        mult = i*sq
        if sp:
            if mult >= 0 and mult < 10:
                req = " " * (mino - 1)
                res.append(req + str(mult))
            else:
                res.append(mult)
        else:
            res.append(mult)
    return res


def rule():
    z = PrettyTable()
    z._set_field_names(['First', 'Mark', 'Second', 'NL', 'Example'])
    z.add_row(['+', 'x', '+', 'two positives make a positive', '3 x 2 = 6'])
    z.add_row(['-', 'x', '-', 'two negatives make a positive', '(-3) x (-2) = 6'])
    z.add_row(['-', 'x', '+', 'a negative and a positive make a negative', '(-3) x 2 = -6'])
    z.add_row(['+', 'x', '-', 'a positive and a negative make a negative', '3 x (-2) = -6'])
    print(z)


def mul_table(form: int) -> str:
    # SRC:: https://www.mathsisfun.com/definitions/multiplication-tables.html
    """
    Generate Table n* to n*
    CERR: 0 < input n > 100
    form: n -> 3
    EXP::  +-----+-----+-----+
           |  1  |  2  |  3  |
           +-----+-----+-----+
           |  1  |  2  |  3  |
                   ...
    """
    assert form > 0
    assert form < 40, "Let prettyTable looks pretty"

    head = [j for j in range(1, form+1)]
    x = PrettyTable()
    x._set_field_names(head)

    for i in range(1, form+1):
        x.add_row(_loop(head, i, False))
    print(x)


def negmul_table(form: str) -> str:
    # SRC:: https://www.mathsisfun.com/multiplying-negatives.html
    """
    Generate Table -n* to n*
    form: n -> -2x2
    EXP::  +-----+-----+-----+-----+-----+-----+
           |  X  | -2  | -1  |  0  |  1  |  2  |
           +-----+-----+-----+-----+-----+-----+
           | -2  |  4  |  2  |  0  | -2  | -4  |
                            ...
    """
    assert isinstance(form, str)
    st, sp = form.split('x')
    start, stop = int(st), int(sp) + 1
    assert start > -30
    assert stop < 30, "It nah looks good on Screen"

    head = _tlike(start, stop)
    lhead = [j for j in range(start, stop)]
    y = PrettyTable()
    y._set_field_names(["X", *lhead])

    for e, i in enumerate(range(start, stop)):
        y.add_row([head[e]] + _loop(lhead, i, True))
    print(y)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-mt", help="generate Multiplication Table", type=int)
    parser.add_argument(
        "-nmt",
        help="generate Multiplication Table from Negative", type=str
    )
    args = parser.parse_args()

    mt = args.mt
    nmt = args.nmt

    if mt:
        mul_table(mt)

    if nmt:
        negmul_table(nmt)

    if not mt and not nmt:
        print("multiplication_tables -h")

