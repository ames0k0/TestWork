#/usr/bin/env python
# -*- coding: utf-8 -*-

# kurenaif <3
# IJ[K]LMNOPQRSTUVWXYZABCDEFGH
# ST[U]VWXYZABCDEFGHIJKLMNOPQR
# PQ[R]STUVWXYZABCDEFGHIJKLMNO
# CD[E]FGHIJKLMNOPQRSTUVWXYZAB
# LM[N]OPQRSTUVWXYZABCDEFGHIJK
# YZ[A]BCDEFGHIJKLMNOPQRSTUVWX
# GH[I]JKLMNOPQRSTUVWXYZABCDEF
# DE[F]GHIJKLMNOPQRSTUVWXYZABC


# TODO: (colored) animation ?


def find(seq, t):
    try:
        return seq.index(t)
    except ValueError:
        return -1


def main(seq: str, target: str, K: int):
    seq = list(seq)
    res = []

    def seq_p(t):
        a = ''.join(seq)
        a = a.replace(t, f'[{t}]')
        print(a)

    seq_p(seq[K])
    print('\n')

    for t in target:
        t_idx = find(seq, t)

        if t_idx == -1:
            continue

        diff = K - t_idx
        res.append(abs(diff))

        if t_idx < K:
            for _ in range(diff):
                seq.insert(0, seq.pop())
        else:
            for _ in range(abs(diff)):
                seq.append(seq.pop(0))

        seq_p(t)
        continue

    print(' '.join([str(r) for r in res]))


if __name__ == '__main__':
    from string import ascii_uppercase

    K = 3
    seq = ascii_uppercase
    target = 'kurenaif'.upper()
    main(seq, target, K)

    exit()

    for K in range(len(seq)):
        print('\n')
        main(seq, target, K)
